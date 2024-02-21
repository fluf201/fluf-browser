import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction, QTabWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage

class AdBlocker(QWebEnginePage):
    def __init__(self, profile):
        super().__init__(profile)
        self.blocked_domains = [
            'advertising-api-eu.amazon.com',
            'pagead2.googlesyndication.com',
            'afs.googlesyndication.com',
            'adservice.google.com',
            'stats.g.doubleclick.net',
            'pagead2.googleadservices.com',
            'analyticsengine.s3.amazonaws.com',
            'adtago.s3.amazonaws.com',
            'advice-ads.s3.amazonaws.com',
            'google-analytics.com',
            'ssl.google-analytics.com',
            'adservetx.media.net',
            'adm.hotjar.com',
            'ads30.adcolony.com',
            'events3alt.adcolony.com',
            'adc3-launch.adcolony.com',
            'wd.adcolony.com',
            'analytics.google.com',
            'static.doubleclick.net',
            'static.media.net',
            'analytics.s3.amazonaws.com',
            'click.googleanalytics.com',
            'ad.doubleclick.net',
            'surveys.hotjar.com',
            'insights.hotjar.com',
            'script.hotjar.com',
            'm.doubleclick.net',
            'events.hotjar.io',
            'cdn.mouseflow.com',
            'identify.hotjar.com',
            'mouseflow.com',
            'api.luckyorange.com',
            'o2.mouseflow.com',
            'api.mouseflow.com',
            'upload.luckyorange.net',
            'cs.luckyorange.net',
            'settings.luckyorange.net',
            'cdn-test.mouseflow.com',
            'browser.sentry-cdn.com',
            'an.facebook.com',
            'sessions.bugsnag.com',
            'notify.bugsnag.com',
            'freshmarketer.com',
            'api.bugsnag.com',
            'cdn.luckyorange.com',
            'w1.luckyorange.com',
            'pixel.facebook.com',
            'static.ads-twitter.com',
            'log.pinterest.com',
            'events.reddit.com',
            'widgets.pinterest.com',
            'analytics.pinterest.com',
            'app.bugsnag.com',
            'fwtracks.freshmarketer.com',
            'ads.pinterest.com',
            'ads-api.twitter.com',
            'ads.yahoo.com',
            'udcm.yahoo.com',
            'udc.yahoo.com',
            'analytics.query.yahoo.com',
            'geo.yahoo.com',
            'analytics.tiktok.com',
            'trk.pinterest.com',
            'app.getsentry.com',
            'business-api.tiktok.com',
            'ads-api.tiktok.com',
            'ads.tiktok.com',
            'log.fc.yahoo.com',
            'analytics-sg.tiktok.com',
            'events.redditmedia.com',
            'log.byteoversea.com',
            'webview.unityads.unity3d.com',
            'ads-sg.tiktok.com',
            'auction.unityads.unity3d.com',
            'adserver.unityads.unity3d.com',
            'config.unityads.unity3d.com',
            'gemini.yahoo.com',
            'appmetrica.yandex.ru',
            'adfstat.yandex.ru',
            'adfox.yandex.ru',
            'extmaps-api.yandex.net',
            'iot-eu-logser.realme.com',
            'offerwall.yandex.net',
            'metrika.yandex.ru',
            'sdkconfig.ad.xiaomi.com',
            'sdkconfig.ad.intl.xiaomi.com',
            'api.ad.xiaomi.com',
            'data.mistat.xiaomi.com',
            'data.mistat.india.xiaomi.com',
            'data.mistat.rus.xiaomi.com',
            'bdapi-in-ads.realmemobile.com',
            'iot-logser.realme.com',
            'bdapi-ads.realmemobile.com',
            'logservice.hicloud.com',
            'metrics2.data.hicloud.com',
            'metrics.data.hicloud.com',
            'grs.hicloud.com',
            'smetrics.samsung.com',
            'samsung-com.112.2o7.net',
            'open.oneplus.net',
            'nmetrics.samsung.com',
            'iadsdk.apple.com',
            'tracking.rus.miui.com',
            'logbak.hicloud.com',
            'logservice1.hicloud.com',
            'ck.ads.oppomobile.com',
            'adx.ads.oppomobile.com',
            'partnerads.ysm.yahoo.com',
            'data.ads.oppomobile.com',
            'metrics.icloud.com',
            'metrics.mzstatic.com',
            'ads.youtube.com',
            'media.net',
            'analytics.yahoo.com',
            'mediavisor.doubleclick.net',
            'adsfs.oppomobile.com',
            'stats.wp.com',
            'advertising.yandex.ru',
            'tools.mouseflow.com',
            'careers.hotjar.com',
            'books-analytics-events.apple.com',
            'weather-analytics-events.apple.com',
            'notes-analytics-events.apple.com',
            'api-adservices.apple.com',
            'analytics.pointdrive.linkedin.com',
            'advertising.yahoo.com',
            'click.oneplus.cn',
            'ads.linkedin.com',
            'advertising.apple.com',
            'analytics-api.samsunghealthcn.com',
            'samsungads.com',
            'adtech.yahooinc.com'
            # Add more ad domains as needed
        ]

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if isMainFrame:
            for domain in self.blocked_domains:
                if domain in url.toString():
                    return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.setDocumentMode(True)
        self.tabs.tabBar().setDrawBase(False)
        self.setCentralWidget(self.tabs)

        self.search_history = []

        self.load_search_history()

        self.add_tab("http://www.google.com")

        self.navbar = QToolBar()
        self.addToolBar(self.navbar)

        # New Tab Button
        self.new_tab_action = QAction("+", self)
        self.new_tab_action.triggered.connect(self.add_new_tab)
        self.navbar.addAction(self.new_tab_action)

        # Search History Button
        self.search_history_action = QAction("Search History", self)
        self.search_history_action.triggered.connect(self.show_search_history)
        self.navbar.addAction(self.search_history_action)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        self.navbar.addWidget(self.url_bar)

        self.go_button = QAction("Go", self)
        self.go_button.triggered.connect(self.navigate_url)
        self.navbar.addAction(self.go_button)

        self.show()

    def add_tab(self, url):
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))
        self.tabs.addTab(browser, "New Tab")

    def add_new_tab(self):
        self.add_tab("about:blank")

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()

    def navigate_url(self):
        current_browser = self.tabs.currentWidget()
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        current_browser.setUrl(QUrl(url))
        self.search_history.append(url)
        self.save_search_history()

    def load_search_history(self):
        try:
            with open('searchhistory.txt', 'r') as file:
                self.search_history = file.readlines()
        except FileNotFoundError:
            pass

    def save_search_history(self):
        with open('searchhistory.txt', 'w') as file:
            file.writelines(self.search_history)

    def show_search_history(self):
        history_text = '\n'.join(self.search_history)
        QMessageBox.information(self, "Search History", history_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec_())