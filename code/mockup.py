import os
import sys
import model_run_gui


from PyQt5 import QtCore, QtGui, QtWidgets
#from QtWidgets import QFileDialog
from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication

# Path to this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import sys

class SecondWindow(QtWidgets.QDialog):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		uic.loadUi("DictSelection.ui", self)
		self.checkBox_MercedesAMG.setChecked(MyWindow.use_MercedesAMG)
		self.checkBox_rogerfederer.setChecked(MyWindow.use_rogerfederer)
		self.checkBox_realDonaldTrump.setChecked(MyWindow.use_realDonaldTrump)
		self.checkBox_Forbes.setChecked(MyWindow.use_Forbes)
		
		self.show()

	def setMercedesAMG(self):
		MyWindow.use_MercedesAMG = self.checkBox_MercedesAMG.isChecked()
		print("setMercedesAMG = {}".format(MyWindow.use_MercedesAMG))
		pass
	
	def setrogerfederer(self):
		MyWindow.use_rogerfederer = self.checkBox_rogerfederer.isChecked()
		print("setsetrogerfederer = {}".format(MyWindow.use_rogerfederer))
		pass
	
	def setrealDonaldTrump(self):
		MyWindow.use_realDonaldTrump = self.checkBox_realDonaldTrump.isChecked()
		print("setrealDonaldTrump = {}".format(MyWindow.use_realDonaldTrump))
		pass

	def setForbes(self):
		MyWindow.use_Forbes = self.checkBox_Forbes.isChecked()
		print("setForbes = {}".format(MyWindow.use_Forbes))
		pass

	



class MyWindow(QtWidgets.QMainWindow):

	liveCorrection = False

	use_MercedesAMG = True
	use_rogerfederer = True
	use_realDonaldTrump = True
	use_Forbes = True

	@staticmethod
	def getDictList():
		input_dicts = []
		# Choose the dicts to append as input
		if MyWindow.use_MercedesAMG:
			input_dicts.append('clean_MercedesAMG')
			print('clean_MercedesAMG')
		if MyWindow.use_rogerfederer:
			input_dicts.append('clean_rogerfederer')
			print('clean_rogerfederer')
		if MyWindow.use_realDonaldTrump:
			input_dicts.append('clean_realDonaldTrump')
			print('clean_realDonaldTrump')
		if MyWindow.use_Forbes:
			input_dicts.append('clean_Forbes')
			print('clean_Forbes')
		print(input_dicts)	
		return input_dicts

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		uic.loadUi("gui.ui", self)
		self.show()
	


	def input_word(self):
		if self.liveCorrection:
			stringIn = self.input.toPlainText()
			if stringIn:
				if not model_run_gui.existsModel(self.getDictList()):
					self.label_ModelGeneration.setText("Generating Model ...")
					QtWidgets.QMessageBox.about(self, "Info", "Model doesn't exists in memory, additional computation time is required")
				self.label_ModelGeneration.setText("Model generated successfully!")					
				result = model_run_gui.tryViterbi(stringIn,self.getDictList())
				self.output.setText(result)
			else:
				self.output.setText("")
		pass

	def push_correction(self):
		if not self.liveCorrection:
			print(self.input.toPlainText())
			stringIn = self.input.toPlainText()
			if stringIn:
				if not model_run_gui.existsModel(self.getDictList()):
					self.label_ModelGeneration.setText("Generating Model ...")
					QtWidgets.QMessageBox.about(self, "Info", "Model doesn't exists in memory, additional computation time is required")
				self.label_ModelGeneration.setText("Model generated successfully!")
				result = model_run_gui.tryViterbi(stringIn,self.getDictList())
				self.output.setText(result)
			else:
				self.output.setText("")
		pass

	def predicted_word(self):
		pass

	def setLiveCorrection(self):
		print(self.checkBoxLiveCorrection.isChecked())
		self.liveCorrection = self.checkBoxLiveCorrection.isChecked()
		pass

	def getFile(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		# fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QtWidgets.QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QtWidgets.QFileDialog.getOpenFileName()", "","Text files (*.txt)", options=options)
		if fileName:
			print(fileName)
			f = open(fileName, 'r', encoding='UTF-8')
			with f:
				data = f.read()
			self.input.setText(data)

	def openDialog(self):
		print("proova")
		self.ui = SecondWindow()
		# self.window.show()


if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())
