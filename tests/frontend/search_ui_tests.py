import os
import shutil
import unittest
from pathlib import Path
from src.frontend.app import app
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.frontend.ui_tests_base import UITestsBase
from src.backend import MockQuery
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class SearchUITests(UITestsBase):
    """Search UI tests.
    Tests that the search bar works as expected.
    """

    def setUp(self):
        """Setup
        """
        self.output_path = str(Path('tests/frontend/queries/').absolute())
        shutil.rmtree(self.output_path, ignore_errors=True)
        self.query = MockQuery()

        for _ in range(10):
            self.full_filename = self.query.query_and_update(self.output_path)[
                0]

        self.filename = Path(self.full_filename).name
        super().setUp()
        self.search_input = self.driver.find_element_by_id('input-search-logs')

    def tearDown(self):
        """Teardown
        """
        shutil.rmtree(self.output_path, ignore_errors=True)
        super().tearDown()

    def search(self, path: str):
        """Clears and searches using the search bar
        """
        self.search_input.clear()
        self.search_input.send_keys(path)
        self.wait_for_ajax_to_complete()

    @unittest.skip("Not debugging currently.")
    def test_searching_logs(self):
        """Test searching for the mock logs.
        """
        self.search(self.output_path)
        self.wait_for_element(By.ID, self.filename)

        path_ending_on_slash = os.path.join(self.output_path, '')
        self.search(path_ending_on_slash)
        self.wait_for_element(By.ID, self.filename)

        self.search('    ' + path_ending_on_slash + '     ')
        self.wait_for_element(By.ID, self.filename)

        incomplete_path = self.output_path[:-2]
        self.search(incomplete_path)
        with self.assertRaises(TimeoutException):
            self.wait_for_element(By.ID, self.filename)

    def test_indices_correct_displayed(self):
        """Test searching for the mock logs.
        """
        self.search(self.output_path)
        self.click_element(By.ID, self.filename)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
