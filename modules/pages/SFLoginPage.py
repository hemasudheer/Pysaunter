'''
Created on Oct 22, 2014

@author: hemasudheer
'''


from modules.pages.SFBasePage import SFBasePage
import time

locators = {"username": "//input[@id='username']",
            "password": "//*[@id='password']",
            "login_button": "//*[@id='Login']",
            "home_tab": "//*[@id='home_Tab']",
            }


class SFLoginPage(SFBasePage):

    def do_login(self):
        self.get_url(self.get_config('SF_login_url'))
        time.sleep(5)
        self.type(locators["username"], self.get_config('SF_username', 'Credentials'))
        self.type(locators["password"], self.get_config('SF_password', 'Credentials'))
        self.press(locators["login_button"])

    def is_logged_in(self):
        self.wait_in_seconds(10)
        self.is_element_present(locators["home_tab"])
