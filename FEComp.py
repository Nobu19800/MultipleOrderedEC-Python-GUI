# -*- coding: cp932 -*-
from PyQt4 import QtCore, QtGui


##
#����u���b�N�̃E�B�W�F�b�g
##
class FEComp(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FEComp, self).__init__(parent)
        self.ECS = []
        self.CL = QtGui.QVBoxLayout()
        
        self.setLayout(self.CL)

        
