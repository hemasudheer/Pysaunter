
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from saunter.po import timeout_seconds
from saunter.po.webdriver.page import Page as SaunterPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import saunter
import time

parser = saunter.ConfigWrapper.ConfigWrapper().config


class Page(SaunterPage):

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def get_config(self, key, section=None):
        if section == None:
            return parser.get('TestData', key)
        else:
            return parser.get(section, key)

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
