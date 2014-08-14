# -*- coding: cp932 -*-

from PyQt4 import QtCore, QtGui
from FEComp import FEComp

##
#�u���b�N�ǉ��{�^�����܂ރE�B�W�F�b�g
##
class AddButton(QtGui.QWidget):
    clicked = QtCore.pyqtSignal("FEComp")
    def __init__(self, text, parent=None):
        super(AddButton, self).__init__(parent)
        
        self.Fc = None
        self.PB = QtGui.QPushButton(text)
        self.mainLayout = QtGui.QVBoxLayout()
        
        #connect(PB, SIGNAL(clicked()),
        #    this, SLOT(clickedSlot()))
        #QtCore.QObject.connect(self.PB, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("clickedSlot()"))

        self.PB.clicked.connect(self.clickedSlot)

        self.mainLayout.addWidget(self.PB)

        self.setLayout(self.mainLayout)

        
        
    ##
    #�{�^���N���b�N���ɌĂяo���X���b�g
    ##
    def clickedSlot(self):
        print self.Fc
        self.clicked.emit(self.Fc)
