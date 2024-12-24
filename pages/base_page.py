from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def wait_for_element(self, how, what, timeout=20):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((how, what))
        )
