# -*- coding: utf-8 -*- 
 
# Form implementation generated from reading ui file 'GUI.ui' 
# 
# Created by: PyQt5 UI code generator 5.9.2 
# 
# WARNING! All changes made in this file will be lost! 
 
from PyQt5 import QtCore, QtGui, QtWidgets 
import os 
import utility_gui 
from configparser import ConfigParser 
from models_IO import io_model 
from generate_model import create_model 
from generate_model import model 
from generate_model import viterbi_compute 
from configparser import ConfigParser 
 
 
class Ui_MainWindow(QtWidgets.QMainWindow):  # codice da non guardare 
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("MainWindow") 
        MainWindow.resize(402, 550) 
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
        self.centralwidget.setObjectName("centralwidget") 
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget) 
        self.horizontalLayout_2.setObjectName("horizontalLayout_2") 
        self.verticalLayout = QtWidgets.QVBoxLayout() 
        self.verticalLayout.setObjectName("verticalLayout") 
        self.frame = QtWidgets.QFrame(self.centralwidget) 
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel) 
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised) 
        self.frame.setObjectName("frame") 
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame) 
        self.verticalLayout_3.setObjectName("verticalLayout_3") 
        self.horizontalLayout = QtWidgets.QHBoxLayout() 
        self.horizontalLayout.setObjectName("horizontalLayout") 
        self.lineEdit = QtWidgets.QLineEdit(self.frame) 
        self.lineEdit.setObjectName("lineEdit") 
        self.horizontalLayout.addWidget(self.lineEdit) 
        self.pushButtonAsk = QtWidgets.QPushButton(self.frame) 
        self.pushButtonAsk.setObjectName("pushButtonAsk") 
        self.horizontalLayout.addWidget(self.pushButtonAsk) 
        self.pushButton = QtWidgets.QPushButton(self.frame) 
        self.pushButton.setObjectName("pushButton") 
        self.horizontalLayout.addWidget(self.pushButton) 
        self.verticalLayout_3.addLayout(self.horizontalLayout) 
        self.verticalLayout.addWidget(self.frame) 
        self.frame_2 = QtWidgets.QFrame(self.centralwidget) 
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel) 
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised) 
        self.frame_2.setObjectName("frame_2") 
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2) 
        self.verticalLayout_2.setObjectName("verticalLayout_2") 
        self.label = QtWidgets.QLabel(self.frame_2) 
        self.label.setObjectName("label") 
        self.verticalLayout_2.addWidget(self.label) 
        self.plainTextEdit = QtWidgets.QTextEdit(self.frame_2) 
        self.plainTextEdit.setMinimumSize(QtCore.QSize(350, 350)) 
        self.plainTextEdit.setObjectName("plainTextEdit") 
        self.verticalLayout_2.addWidget(self.plainTextEdit) 
        self.verticalLayout.addWidget(self.frame_2) 
        self.horizontalLayout_2.addLayout(self.verticalLayout) 
        MainWindow.setCentralWidget(self.centralwidget) 
        self.statusbar = QtWidgets.QStatusBar(MainWindow) 
        self.statusbar.setObjectName("statusbar") 
        MainWindow.setStatusBar(self.statusbar) 
        self.menuBar = QtWidgets.QMenuBar(MainWindow) 
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 402, 22)) 
        self.menuBar.setStatusTip("") 
        self.menuBar.setObjectName("menuBar") 
        self.menuSettings = QtWidgets.QMenu(self.menuBar) 
        self.menuSettings.setStatusTip("") 
        self.menuSettings.setObjectName("menuSettings") 
        self.menuDatabases = QtWidgets.QMenu(self.menuBar) 
        self.menuDatabases.setStatusTip("") 
        self.menuDatabases.setObjectName("menuDatabases") 
        MainWindow.setMenuBar(self.menuBar) 
        self.actionLive_Correction = QtWidgets.QAction(MainWindow) 
        self.actionLive_Correction.setCheckable(True) 
        self.actionLive_Correction.setMenuRole(QtWidgets.QAction.TextHeuristicRole) 
        self.actionLive_Correction.setObjectName("actionLive_Correction") 
        self.actionMercedes_AMG = QtWidgets.QAction(MainWindow) 
        self.actionMercedes_AMG.setCheckable(True) 
        self.actionMercedes_AMG.setObjectName("actionMercedes_AMG") 
        self.actionRogerfederer = QtWidgets.QAction(MainWindow) 
        self.actionRogerfederer.setCheckable(True) 
        self.actionRogerfederer.setObjectName("actionRogerfederer") 
        self.actionRealdonaldTrump = QtWidgets.QAction(MainWindow) 
        self.actionRealdonaldTrump.setCheckable(True) 
        self.actionRealdonaldTrump.setObjectName("actionRealdonaldTrump") 
        self.actionForbes = QtWidgets.QAction(MainWindow) 
        self.actionForbes.setCheckable(True) 
        self.actionForbes.setObjectName("actionForbes") 
        self.menuSettings.addAction(self.actionLive_Correction) 
        self.menuDatabases.addAction(self.actionMercedes_AMG) 
        self.menuDatabases.addAction(self.actionRogerfederer) 
        self.menuDatabases.addAction(self.actionRealdonaldTrump) 
        self.menuDatabases.addAction(self.actionForbes) 
        self.menuBar.addAction(self.menuSettings.menuAction()) 
        self.menuBar.addAction(self.menuDatabases.menuAction()) 
 
        ######### codice da guardare######## 
 
        # menu bar actions preset 
        self.actionLive_Correction.setChecked(True) 
        self.actionForbes.setChecked(True) 
        self.actionMercedes_AMG.setChecked(True) 
        self.actionRogerfederer.setChecked(True) 
        self.actionRealdonaldTrump.setChecked(True) 
 
        self.retranslateUi(MainWindow) # retranslator 
 
        self.pushButton.clicked.connect(self.get_file) # buttons bindings  
        self.pushButtonAsk.clicked.connect(self.ask_result) 
 
        self.lineEdit.textEdited.connect(self.pushButtonAsk.click) #  check atuomatico 
        self.lineEdit.returnPressed.connect(self.pushButtonAsk.click)  
        self.actionLive_Correction.changed.connect(self.set_live_checking) 
 
        self.actionForbes.changed.connect(self.load_dictionaries) # menubar actions bindings 
        self.actionMercedes_AMG.changed.connect(self.load_dictionaries) 
        self.actionRogerfederer.changed.connect(self.load_dictionaries) 
        self.actionRealdonaldTrump.changed.connect(self.load_dictionaries) 
 
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
 
        self.load_dictionaries() # preloading of the dictionary 
 
 
    def retranslateUi(self, MainWindow): 
        _translate = QtCore.QCoreApplication.translate 
        MainWindow.setWindowTitle(_translate("MainWindow", "Mispeller")) 
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type a word...")) 
        self.pushButtonAsk.setStatusTip(_translate("MainWindow", "Look for a possible match")) 
        self.pushButtonAsk.setText(_translate("MainWindow", "Search")) 
        self.pushButton.setStatusTip(_translate("MainWindow", "Load a Txt file")) 
        self.pushButton.setText(_translate("MainWindow", "Load")) 
        self.label.setText(_translate("MainWindow", "Result")) 
        self.menuSettings.setTitle(_translate("MainWindow", "Settings")) 
        self.menuDatabases.setTitle(_translate("MainWindow", "Databases")) 
        self.actionLive_Correction.setText(_translate("MainWindow", "Live Correction")) 
        self.actionLive_Correction.setStatusTip(_translate("MainWindow", "Disable/Enable Live Correction")) 
        self.actionMercedes_AMG.setText(_translate("MainWindow", "Mercedes AMG")) 
        self.actionMercedes_AMG.setStatusTip(_translate("MainWindow", "Enable/Disable this Dataset")) 
        self.actionRogerfederer.setText(_translate("MainWindow", "rogerfederer")) 
        self.actionRogerfederer.setStatusTip(_translate("MainWindow", "Enable/Disable this Dataset")) 
        self.actionRealdonaldTrump.setText(_translate("MainWindow", "realdonaldTrump")) 
        self.actionRealdonaldTrump.setStatusTip(_translate("MainWindow", "Enable/Disable this Dataset")) 
        self.actionForbes.setText(_translate("MainWindow", "Forbes")) 
        self.actionForbes.setStatusTip(_translate("MainWindow", "Enable/Disable this Dataset")) 
 
    def get_file(self): 
        options = QtWidgets.QFileDialog.Options() 
        options = QtWidgets.QFileDialog.DontUseNativeDialog 
        fileName, _filter = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;TXT files (*.txt)", options=options) 
        if fileName: 
            print(fileName) 
            result = viterbi_compute.file_correction(self.model,fileName) 
            self.plainTextEdit.clear() 
            self.plainTextEdit.append(''.join(result)) 
 
    def set_live_checking(self): 
        if(self.actionLive_Correction.isChecked()): 
            self.lineEdit.textEdited.connect(self.pushButtonAsk.click) 
        else: 
            self.lineEdit.textEdited.disconnect(self.pushButtonAsk.click)  
 
    def ask_result(self): 
        text = self.lineEdit.text() 
        if(len(text)==0): 
            pass 
        else: 
            result = viterbi_compute.word_correction(self.model, text) 
            print(result) 
            self.plainTextEdit.clear() 
            self.plainTextEdit.append(''.join(result)) 
 
 
 
    def load_dictionaries(self): 
        config = ConfigParser() 
        config.read('./code/config.ini') 
 
        # # Set to true for recomputing the model even if it exists 
        # force_model_computing = False 
 
        # Name of qwerty layout Json 
        input_layout = 'qwerty_simple' 
 
        input_dicts = [] 
        # Choose the dicts to append as input if checked in the menu 
        if(self.actionMercedes_AMG.isChecked()): 
            input_dicts.append('clean_MercedesAMG') 
            print('clean_MercedesAMG') 
        if(self.actionRealdonaldTrump.isChecked()): 
            input_dicts.append('clean_realDonaldTrump') 
            print('clean_realDonaldTrump') 
        if(self.actionRogerfederer.isChecked()): 
            input_dicts.append('clean_rogerfederer') 
            print('clean_rogerfederer') 
        if(self.actionForbes.isChecked()): 
            input_dicts.append('clean_Forbes') 
            print('clean_Frobes') 
 
        #Create the model 
        self.model = utility_gui.launch_model_creation(input_dicts,input_layout,'DizionarioDiProva') 
 
 
 
if __name__ == "__main__": 
    # Path to this file 
    abspath = os.path.abspath(__file__) 
    dname = os.path.dirname(abspath) 
    os.chdir(dname) 
 
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow) 
    MainWindow.show() 
    sys.exit(app.exec_()) 