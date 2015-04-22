import sys

from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import simplejson as json
from traceroute import TraceRoute

from geolocate import GeolocateQuery
import visual_traceroute_ui


# todo
# - unit testing
# - migrate to Qt5
# - only works with IP4, look at IP6
# - fix up invalid url handling
# - move stuff to config file (commands, google maps key, etc)
# - documentation
# - async handling of stderr (same as stdout)
# - add "are you sure" to the close button
# - fix up traceroute output parsing



html = '''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true"></script>
    <script>

  var flightPlanCoordinates = [
    new google.maps.LatLng(37.772323, -122.214897),
    new google.maps.LatLng(21.291982, -157.821856),
    new google.maps.LatLng(-18.142599, 178.431),
    new google.maps.LatLng(-27.46758, 153.027892)
  ];

function initialize() {
  var mapOptions = {
    zoom: 3,
    center: new google.maps.LatLng(0, -180),
    mapTypeId: google.maps.MapTypeId.TERRAIN
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  flightPath.setMap(map);

  for (i = 0; i < flightPlanCoordinates.length; i++) {
      var marker = new google.maps.Marker({
          position: flightPlanCoordinates[i],
          map: map,
          title: 'Hello World!'
      });
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
'''




class VisualTraceRoute(QMainWindow, visual_traceroute_ui.Ui_visual_traceroute_main_window):
    def __init__(self):
        super(VisualTraceRoute, self).__init__()
        self.setupUi(self)
        self.statusbar.show()

        # set up buttons
        self.doLookupPushButton.clicked.connect(self.handle_do_it_button)
        self.closePushButton.clicked.connect(app.exit)

        self.updaterMutex = QtCore.QMutex()

        # set up worker threads for running commands
        self.traceroute_handler = None


    def handle_do_it_button(self):
        try:
            self.statusbar.clearMessage()
            self.statusbar.showMessage("Working...")
            self.doLookupPushButton.setEnabled(False)

            url = self.get_url()
            if url:
                # traceroute
                self.perform_traceroute(url)
            else:
                self.statusbar.showMessage("URL is empty", 5000)

        except Exception as e:
            QMessageBox.critical(self,
                         "Critical",
                         "Problem performing network lookup : " + str(e))


    def all_processes_terminated(self):
        self.doLookupPushButton.setEnabled(True)
        self.doLookupPushButton.update()
        self.statusbar.clearMessage()
        self.statusbar.showMessage("Complete!")

        print(self.route_list)
        self.draw_visual_trace_route()



    def draw_visual_trace_route(self):
        # set up for visual traceroute
        hbx = QHBoxLayout()
        self.visualTraceRouteWidget.setLayout(hbx)
        web = QWebView()
        web.setHtml(html)
        hbx.addWidget(web)
        web.show()



    def add_results(self, command_type, command_output):
        try:
            self.updaterMutex.lock()

            if command_type == CommandTypes.Ping:
                self.pingTextBrowser.moveCursor(QTextCursor.End)
                self.pingTextBrowser.insertPlainText(command_output)
            elif command_type == CommandTypes.Dig:
                self.dnsTextBrowser.moveCursor(QTextCursor.End)
                self.dnsTextBrowser.insertPlainText(command_output)
            elif command_type == CommandTypes.nslookup:
                self.nslookupTextBrowser.moveCursor(QTextCursor.End)
                self.nslookupTextBrowser.insertPlainText(command_output)
            elif command_type == CommandTypes.Geolocate:
                text = json.dumps(command_output, sort_keys=True, indent=4)
                self.geolocateTextBrowser.moveCursor(QTextCursor.End)
                self.geolocateTextBrowser.insertPlainText(str(text))

        except Exception as e:
            QMessageBox.critical(self,
                                 "Critical",
                                 "Problem updating UI with command output : " + str(e))
        finally:
            self.updaterMutex.unlock()


    def perform_traceroute(self, url):
        try:
            self.traceroute_handler = TraceRoute(url)
            self.connect(self.traceroute_handler, QtCore.SIGNAL("TraceRoute"), self.add_results)
            self.traceroute_handler.start()
        except Exception as e:
            QMessageBox.critical(self,
                                 "Critical",
                                 "Problem performing TraceRoute command : " + str(e))


    def handle_trace_route(self, output):
        print(output)

        line = str(output).strip()

        if line[:1] in '0123456789':
            # this line is a route
            if "*" not in line:
                # line has a valid route IP
                if ')' in line and '(' in line:
                    # find IP address and save it
                    start_idx = line.index('(')
                    end_idx = line.index(')')
                    ip_addr = line[start_idx + 1:end_idx]
                    self.route_list.append(ip_addr)



    def get_url(self):
        # todo - validate url input and prompt dialog
        return self.urlLineEdit.text()


app = QApplication(sys.argv)
nu = VisualTraceRoute()
nu.show()
app.exec_()
