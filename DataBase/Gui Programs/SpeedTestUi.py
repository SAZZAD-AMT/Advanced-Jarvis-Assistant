from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpeedTest(object):

    def setupUi(self, SpeedTest):

        SpeedTest.setObjectName("SpeedTest")
        SpeedTest.resize(582, 335)
        self.centralwidget = QtWidgets.QWidget(SpeedTest)
        self.centralwidget.setObjectName("centralwidget")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(-10, 0, 601, 341))
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("E:\\YouTube Channel\\YouTube - Jarvis\\How To Make Jarvis In Python\\DataBase\\Gui Materials\\speedTest.gif"))
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        SpeedTest.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpeedTest)
        QtCore.QMetaObject.connectSlotsByName(SpeedTest)

    def retranslateUi(self, SpeedTest):
        _translate = QtCore.QCoreApplication.translate
        SpeedTest.setWindowTitle(_translate("SpeedTest", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpeedTest = QtWidgets.QMainWindow()
    ui = Ui_SpeedTest()
    ui.setupUi(SpeedTest)
    SpeedTest.show()
    sys.exit(app.exec_())

