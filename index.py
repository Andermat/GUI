#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QToolTip, QPushButton, QApplication, QAction, qApp, QLabel, QCalendarWidget)
from PyQt5.QtCore import (QCoreApplication, QDate)
from PyQt5.QtGui import (QFont, QIcon)
from pypyodbc import *


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        QToolTip.setFont(QFont('SansSerif', 10))

        #self.setToolTip('Main Dominos window')

        #qbtn = QPushButton('Exit', self)
        #qbtn.setToolTip('Exit application')
        #qbtn.clicked.connect(QCoreApplication.instance().quit)
        #qbtn.resize(btn.sizeHint())
        #qbtn.move(320, 460)

        #self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Dominos Control Center v0.01')
        self.show()
        self.setFixedSize(400, 500)
        self.statusBar().showMessage('Ready')

        exportAction = QAction(QIcon('export.png'), '&Export', self)
        exportAction.setShortcut('Ctrl+E')
        exportAction.setStatusTip('Export data')
        exportAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exportAction)

        btn = QPushButton('Search', self)
        btn.setToolTip('Search some data')
        btn.resize(btn.sizeHint())
        btn.move(1, 30)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

