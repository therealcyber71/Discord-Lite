# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

import time

import time

def class_runner():
	
	class MainWindow(QMainWindow):

	# constructor
		def __init__(self, *args, **kwargs):
			super(MainWindow, self).__init__(*args, **kwargs)


			# creating a QWebEngineView
			self.browser = QWebEngineView()

			# setting default browser url as google
			self.browser.setUrl(QUrl("https://discord.com/app"))
			#self.status = QStatusBar()

			# adding status bar to the main window
			

			

			# adding action when url get changed
			self.browser.urlChanged.connect(self.update_urlbar)

			# adding action when loading is finished
			self.browser.loadFinished.connect(self.update_title)

			# set this browser as central widget or main window
			self.setCentralWidget(self.browser)

			# creating a status bar object
			self.status = QStatusBar()

			# adding status bar to the main window
			self.setStatusBar(self.status)

			#### THE CODE HERE HAS BEEN EDITED FROM THE GEEKS FOR GEEKS TUTORIAL, I WOULD LOVE FOR SOMEONE TO EDIT IT WITHOUT DISTRUBING THE PACKAGE LMAO ####
			

			# adding actions to the tool bar
			# creating a action for back
			back_btn = QAction("Back", self)

			# setting status tip
			back_btn.setStatusTip("Back to previous page")

			# adding action to the back button
			# making browser go back
			back_btn.triggered.connect(self.browser.back)

			# adding this action to tool bar
			

			# similarly for forward action
			next_btn = QAction("Forward", self)
			next_btn.setStatusTip("Forward to next page")

			# adding action to the next button
			# making browser go forward
			next_btn.triggered.connect(self.browser.forward)
			

			# similarly for reload action
			reload_btn = QAction("Reload", self)
			reload_btn.setStatusTip("Reload page")

			# adding action to the reload button
			# making browser to reload
			reload_btn.triggered.connect(self.browser.reload)
			

			# similarly for home action
			home_btn = QAction("Home", self)
			home_btn.setStatusTip("Go home")
			home_btn.triggered.connect(self.navigate_home)
			

			# creating a line edit for the url
			self.urlbar = QLineEdit()

			# adding action when return key is pressed
			self.urlbar.returnPressed.connect(self.navigate_to_url)

			# adding this to the tool bar
			

			# adding stop action to the tool bar
			stop_btn = QAction("Stop", self)
			stop_btn.setStatusTip("Stop loading current page")

			# adding action to the stop button
			# making browser to stop
			stop_btn.triggered.connect(self.browser.stop)
			
			
		# showing all the components
			self.show()

	
	# method for updating the title of the window
		def update_title(self):
			title = self.browser.page().title()
			self.setWindowTitle("% s - on Discord Lite" % title)


		# method called by the home action
		def navigate_home(self):

			# open the google
			self.browser.setUrl(QUrl("httpS://discord.com/app"))

		# method called by the line edit when return key is pressed
		def navigate_to_url(self):

			# getting url and converting it to QUrl object
			q = QUrl(self.urlbar.text())

			# if url is scheme is blank
			if q.scheme() == "":
				# set url scheme to html
				q.setScheme("http")

			# set the url to the browser
			self.browser.setUrl(q)

		
		def update_urlbar(self, q):

			
			self.urlbar.setText(q.toString())

			
			self.urlbar.setCursorPosition(0)		

	app = QApplication(sys.argv)


	app.setApplicationName("Discord Lite")
	scriptDir = os.path.dirname(os.path.realpath(__file__))
	app.setWindowIcon(QIcon(scriptDir + os.path.sep + 'logo4.png'))


	window = MainWindow()


	# start the app

	app.exec_()
class_runner()

