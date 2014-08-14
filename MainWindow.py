# -*- coding: cp932 -*-

from PyQt4 import QtCore, QtGui
from SetComp import SetComp


##
#���C���E�B���h�E�̃E�B�W�F�b�g
##
class MainWindow(QtGui.QMainWindow):
    def __init__(self, ec):
        super(MainWindow, self).__init__()

        self.layout = QtGui.QVBoxLayout()
        self.m_ec = ec
        self.SC = SetComp(self.m_ec)
        
        self.SC.UpdateSizeSignal.connect(self.m_resize)
        self.layout.addWidget(self.SC)

        self.layout.addStretch()
	self.UB = QtGui.QPushButton(u"�X�V")
	self.layout.addWidget(self.UB)

	
	self.UB.clicked.connect(self.UpdateComp)

	self.DB = QtGui.QPushButton(u"�ǉ�")
	self.layout.addWidget(self.DB)

	self.DB.clicked.connect(self.SC.CreateComp)

	
	
        
        self.widget = QtGui.QWidget()
        self.widget.setLayout(self.layout)
        self.area = QtGui.QScrollArea()
        self.area.setWidget(self.widget)
        self.setCentralWidget(self.area)
        self.setWindowTitle("MultipleOrderedECGUI")
        self.setUnifiedTitleAndToolBarOnMac(True)

        self.SC.UpdateSizeSlot()

        self.newAct = None
        self.openAct = None
        self.saveAct = None
        self.fileMenu = None

        self.createAction()
	self.createMenus()

        #self.widget.resize(400, 400)

    ##
    #�T�C�Y��ύX����Ƃ��ɌĂяo�����X���b�g
    ##
    def m_resize(self, w, h):

	self.widget.resize(w, h)

    ##
    #RTC���ǉ��A�폜���ꂽ�Ƃ��ɌĂяo�����X���b�g
    ##
    def UpdateComp(self):

	SC.UpdateComps()
	SC.UpdateComp2()

    ##
    #�A�N�V�����̍쐬�̊֐�
    ##
    def createAction(self):

	self.newAct = QtGui.QAction("&New...",self)
	self.newAct.setShortcuts(QtGui.QKeySequence.New)
        self.newAct.triggered.connect(self.newFile)
        


	self.openAct = QtGui.QAction("&Open...",self)
        self.openAct.setShortcuts(QtGui.QKeySequence.Open)
        self.openAct.triggered.connect(self.open)


        self.saveAct = QtGui.QAction("&Save",self)
        self.saveAct.setShortcuts(QtGui.QKeySequence.Save)
        self.saveAct.triggered.connect(self.save)
        

    ##
    #���j���[�̍쐬�̊֐�
    ##
    def createMenus(self):

	self.fileMenu = self.menuBar().addMenu("&File")
	self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
	



    ##
    #�t�@�C���ǂݍ��݃X���b�g
    ##
    def open(self):

	fileName = QtGui.QFileDialog.getOpenFileName(self,u"�J��","","Config File (*.conf);;Python File (*.py);;All Files (*)")
	

	ba = str(fileName.toLocal8Bit())
	self.SC.open(ba)


    ##
    #�t�@�C���ۑ��̃X���b�g
    ##
    def save(self):

	fileName = QtGui.QFileDialog.getSaveFileName(self,u"�ۑ�", "","Config File (*.conf);;All Files (*)")
	if fileName.isEmpty():
            return False

	ba = str(fileName.toLocal8Bit())
	


        return self.SC.save(ba)


    ##
    #�������̃X���b�g
    ##
    def newFile(self):

	self.SC.newFile()


    


    ##
    #���s������GUI�ɔ��f������֐�
    ##
    def UpdateRTC(self,rs):

	self.SC.UpdateRTC(rs)
	
