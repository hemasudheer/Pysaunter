import time
from pages.base import SiteBase
from tailored.testcase import BasicTestCase

import pytest

class CheckScratch(BasicTestCase):

    @pytest.marks('scratch')
    def test_categories(self):
        base = SiteBase(self.driver).open_default_url()
