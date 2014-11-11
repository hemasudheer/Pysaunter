from pages.base import SiteBase
from tailored.testcase import BasicTestCase

import pytest

class CheckTester(BasicTestCase):

    @pytest.marks('tagname')
    def test_tester(self):
        print "Check Tester"
        #base = SiteBase(self.driver).open_default_url()

