import pytest
import os
from saunter.testcase.webdriver import SaunterTestCase

if "DOCGENERATION" in os.environ:
    from marks import MarksDecorator
    pytest.marks = MarksDecorator


class BasicTestCase(SaunterTestCase):

    def setup_method(self, method):
        super(BasicTestCase, self).setup_method(method)

    def teardown_method(self, method):
        super(BasicTestCase, self).teardown_method(method)
