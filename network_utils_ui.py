# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network_utils_ui.ui'
#
# Created: Sun Apr 12 13:06:56 2015
# by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_networkutils(object):
    def setupUi(self, networkutils):
        networkutils.setObjectName(_fromUtf8("networkutils"))
        networkutils.resize(800, 642)
        self.centralwidget = QtGui.QWidget(networkutils)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 751, 481))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.traceroute = QtGui.QWidget()
        self.traceroute.setObjectName(_fromUtf8("traceroute"))
        self.traceroutetab = QtGui.QTabWidget(self.traceroute)
        self.traceroutetab.setGeometry(QtCore.QRect(0, 0, 751, 451))
        self.traceroutetab.setObjectName(_fromUtf8("traceroutetab"))
        self.textTraceRoute = QtGui.QWidget()
        self.textTraceRoute.setObjectName(_fromUtf8("textTraceRoute"))
        self.tracerouteTextBrowser = QtGui.QTextBrowser(self.textTraceRoute)
        self.tracerouteTextBrowser.setGeometry(QtCore.QRect(0, 0, 751, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.tracerouteTextBrowser.setFont(font)
        self.tracerouteTextBrowser.setObjectName(_fromUtf8("tracerouteTextBrowser"))
        self.traceroutetab.addTab(self.textTraceRoute, _fromUtf8(""))
        self.visualTraceRoute = QtGui.QWidget()
        self.visualTraceRoute.setObjectName(_fromUtf8("visualTraceRoute"))
        self.traceroutetab.addTab(self.visualTraceRoute, _fromUtf8(""))
        self.tabWidget.addTab(self.traceroute, _fromUtf8(""))
        self.pingTab = QtGui.QWidget()
        self.pingTab.setObjectName(_fromUtf8("pingTab"))
        self.pingTextBrowser = QtGui.QTextBrowser(self.pingTab)
        self.pingTextBrowser.setGeometry(QtCore.QRect(0, 0, 751, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pingTextBrowser.setFont(font)
        self.pingTextBrowser.setTabChangesFocus(False)
        self.pingTextBrowser.setAcceptRichText(False)
        self.pingTextBrowser.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.pingTextBrowser.setObjectName(_fromUtf8("pingTextBrowser"))
        self.tabWidget.addTab(self.pingTab, _fromUtf8(""))
        self.dns = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.dns.setFont(font)
        self.dns.setObjectName(_fromUtf8("dns"))
        self.dnsTextBrowser = QtGui.QTextBrowser(self.dns)
        self.dnsTextBrowser.setGeometry(QtCore.QRect(0, 0, 751, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.dnsTextBrowser.setFont(font)
        self.dnsTextBrowser.setObjectName(_fromUtf8("dnsTextBrowser"))
        self.tabWidget.addTab(self.dns, _fromUtf8(""))
        self.webserver = QtGui.QWidget()
        self.webserver.setObjectName(_fromUtf8("webserver"))
        self.webserverTextBrowser = QtGui.QTextBrowser(self.webserver)
        self.webserverTextBrowser.setGeometry(QtCore.QRect(0, 0, 751, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.webserverTextBrowser.setFont(font)
        self.webserverTextBrowser.setObjectName(_fromUtf8("webserverTextBrowser"))
        self.tabWidget.addTab(self.webserver, _fromUtf8(""))
        self.geolocate = QtGui.QWidget()
        self.geolocate.setObjectName(_fromUtf8("geolocate"))
        self.geolocateTextBrowser = QtGui.QTextBrowser(self.geolocate)
        self.geolocateTextBrowser.setGeometry(QtCore.QRect(0, 0, 751, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.geolocateTextBrowser.setFont(font)
        self.geolocateTextBrowser.setObjectName(_fromUtf8("geolocateTextBrowser"))
        self.tabWidget.addTab(self.geolocate, _fromUtf8(""))
        self.nslookup = QtGui.QWidget()
        self.nslookup.setObjectName(_fromUtf8("nslookup"))
        self.nslookupTextBrowser = QtGui.QTextBrowser(self.nslookup)
        self.nslookupTextBrowser.setGeometry(QtCore.QRect(0, 0, 751, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.nslookupTextBrowser.setFont(font)
        self.nslookupTextBrowser.setObjectName(_fromUtf8("nslookupTextBrowser"))
        self.tabWidget.addTab(self.nslookup, _fromUtf8(""))
        self.urlLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.urlLineEdit.setGeometry(QtCore.QRect(20, 20, 331, 27))
        self.urlLineEdit.setObjectName(_fromUtf8("urlLineEdit"))
        self.doLookupPushButton = QtGui.QPushButton(self.centralwidget)
        self.doLookupPushButton.setGeometry(QtCore.QRect(370, 20, 98, 27))
        self.doLookupPushButton.setObjectName(_fromUtf8("doLookupPushButton"))
        self.closePushButton = QtGui.QPushButton(self.centralwidget)
        self.closePushButton.setGeometry(QtCore.QRect(660, 550, 98, 27))
        self.closePushButton.setObjectName(_fromUtf8("closePushButton"))
        networkutils.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(networkutils)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        networkutils.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(networkutils)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        networkutils.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(networkutils)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(networkutils)
        self.tabWidget.setCurrentIndex(1)
        self.traceroutetab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(networkutils)

    def retranslateUi(self, networkutils):
        networkutils.setWindowTitle(_translate("networkutils", "Network Probe Utility", None))
        self.traceroutetab.setTabText(self.traceroutetab.indexOf(self.textTraceRoute),
                                      _translate("networkutils", "Text", None))
        self.traceroutetab.setTabText(self.traceroutetab.indexOf(self.visualTraceRoute),
                                      _translate("networkutils", "Visual", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.traceroute),
                                  _translate("networkutils", "traceroute", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pingTab), _translate("networkutils", "ping", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dns), _translate("networkutils", "dns", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.webserver),
                                  _translate("networkutils", "Web Server ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.geolocate), _translate("networkutils", "Geolocate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nslookup), _translate("networkutils", "nslookup", None))
        self.urlLineEdit.setPlaceholderText(_translate("networkutils", "Enter URL or IP Address", None))
        self.doLookupPushButton.setText(_translate("networkutils", "Do it", None))
        self.closePushButton.setText(_translate("networkutils", "Close", None))
        self.menuFile.setTitle(_translate("networkutils", "File", None))
        self.menuHelp.setTitle(_translate("networkutils", "Help", None))
        self.actionAbout.setText(_translate("networkutils", "About", None))

