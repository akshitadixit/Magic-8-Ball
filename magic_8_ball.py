from PyQt5.QtWidgets import *
from PyQt5 import QtCore 
from PyQt5.QtGui import *
import sys 
from m8b import ANSWER

class Window(QMainWindow): 
	def __init__(self): 
		super(Window,self).__init__()
		self.initUI()

	def action(self):
		self.timer = QtCore.QTimer(self)

		self.gif = QMovie('images/shuffle.gif')
		self.l1.setMovie(self.gif)
		self.gif.start()

		def show():
			self.gif.stop()
			self.p = QPixmap(ANSWER())
			self.l1.setPixmap(self.p) 
			self.l1.resize(self.p.width(), self.p.height())
		
		self.timer.singleShot(3000, show)

	def initUI(self):
		self.setWindowTitle("Magic-8-Ball")
		self.setGeometry(0, 0, 350, 350)  
		self.setMaximumWidth(350)
		self.setMaximumHeight(350)

		self.l1 = QLabel(self) 
		self.p = QPixmap('images/glow (20).png') 
		self.l1.setPixmap(self.p) 
		self.l1.resize(self.p.width(), self.p.height())

		self.b1 = QPushButton(self)
		self.b1.setText("ASK A QUESTION")
		self.b1.setStyleSheet('border-radius: 50;background-color: #c2c2c2; border: 2px solid black')
		self.b1.move(120, 300)
		self.b1.clicked.connect(self.action)

		#move everything to center
		fg = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		fg.moveCenter(cp)
		self.move(fg.topLeft())
  
		# show all the widgets 
		self.show() 

# create pyqt5 app 
App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 
