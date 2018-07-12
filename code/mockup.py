import os
import model_run_gui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication

# Path to this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import sys

class MyWindow(QtWidgets.QMainWindow):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		uic.loadUi("gui.ui", self)
		self.show()


	def input_word(self):
		pass

	def push_correction(self):
		print(self.input.toPlainText())
		stringIn = self.input.toPlainText()
		result = model_run_gui.tryViterbi(stringIn)
		self.output.setText(result)
		pass

	def predicted_word(self):
		pass

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())
