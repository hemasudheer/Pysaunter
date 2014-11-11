from saunter.po.webdriver.page import Page as SaunterPage
from saunter.po import timeout_seconds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

class Page(SaunterPage):

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def find_element_by_locator(self, locator):
        return self.driver.find_element_by_locator(locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements_by_locator(locator)

    def wait_until_loaded(self):
        pass

    def open_default_url(self):
        pass

    def get_referrer(self):
        return self.driver.execute_script('return document.referrer')
