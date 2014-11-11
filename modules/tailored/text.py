from saunter.po.webdriver.text import Text


class Text(Text):

    def __set__(self, obj, val):
        e = obj.driver.find_element_by_locator(self.locator)
        if val == 'clear()':
            e.clear()
        else:
            e.send_keys(val)
