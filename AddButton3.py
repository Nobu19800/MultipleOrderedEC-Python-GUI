# -*- coding: cp932 -*-

from PyQt4 import QtCore, QtGui
from ExComp import CompLayout


##
#����u���b�N�ǉ��{�^�����܂ރE�B�W�F�b�g
##
class AddButton3(QtGui.QWidget):
    clicked = QtCore.pyqtSignal("QtGui.QWidget", "CompLayout")
    def __init__(self, text, parent=None):
        super(AddButton3, self).__init__(parent)
        
        self.Vl = None
        self.c = None
        self.PB = QtGui.QPushButton(text)
        self.mainLayout = QtGui.QVBoxLayout()
        
        #connect(PB, SIGNAL(clicked()),
        #    this, SLOT(clickedSlot()))

        self.PB.clicked.connect(self.clickedSlot)

        self.mainLayout.addWidget(self.PB)

        self.setLayout(self.mainLayout)

    ##
    #�{�^���N���b�N���ɌĂяo���X���b�g
    ##
    def clickedSlot(self):
        print 1
        self.clicked.emit(self.Vl, self.c)
