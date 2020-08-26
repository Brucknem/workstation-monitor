import sys
import unittest
from src.frontend.app import app
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.frontend.ui_tests_base import UITestsBase
from src.backend import MockQuery

class SearchUITests(UITestsBase):
    """Search UI tests.
    Tests that the search bar works as expected.
    """
    
    def setUp(self):
        """Setup
        """
        super().setUp()
        self.query = MockQuery()

        for _ in range(10):
            self.filenames = self.query.query_and_update()

    def test_yeet(self):
        print('yeeet')


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
