from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # nevbar
        navBar = QToolBar()
        self.addToolBar(navBar)

        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navBar.addAction(back_btn)

        reload_btn = QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navBar.addAction(reload_btn)

        forward_btn = QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navBar.addAction(forward_btn)

        home_btn = QAction('Google',self)
        home_btn.triggered.connect(self.nevigate_google)
        navBar.addAction(home_btn)

        home_btn = QAction('Grofied',self)
        home_btn.triggered.connect(self.nevigate_grofied)
        navBar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navBar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    # navbar2

        # navBar2 = QToolBar()
        # self.addToolBar(navBar2)

        # home_btn = QAction('Grofied',self)
        # home_btn.triggered.connect(self.nevigate_home)
        # navBar2.addAction(home_btn)

    def nevigate_grofied(self):
        self.browser.setUrl(QUrl('http://grofied.com'))

    def nevigate_google(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        x = f"http://{url}"
        self.browser.setUrl(QUrl(x))
        # self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('Jaris_Browser')
window = MainWindow()
app.exec_()
