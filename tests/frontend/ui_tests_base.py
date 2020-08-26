import unittest
from contextlib import contextmanager
from multiprocessing import Process
from time import sleep

import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait

from src.frontend.app import app


class UITestsBase(unittest.TestCase):
    """UI tests.
    """

    def setUp(self):
        """Setup
        """
        self.server = None
        try:
            self.driver = webdriver.Firefox()
            self.driver.get("http://127.0.0.1:5000/")
        except WebDriverException:
            self.server = Process(
                target=app.run,
                kwargs={'debug': True, 'use_debugger': True, 'threaded': False,
                        'use_reloader': False})
            self.server.start()
            sleep(1)
            self.driver.get("http://127.0.0.1:5000/")
        self.assertEqual("Workstation Monitor", self.driver.title)

    def tearDown(self):
        """Teardown
        """
        self.driver.get("http://127.0.0.1:5000/shutdown")
        self.driver.close()

        if self.server:
            self.server.terminate()
            self.server.join()

    def wait_for_element(
            self, by: By, selector: str, timeout=5,
            condition: EC = EC.visibility_of_element_located):
        """Waits for an element to be visible.
        """
        return WebDriverWait(
            self.driver, timeout=timeout).until(
            condition((by, selector)))

    def click_element(self, by: By, selector: str, timeout=2):
        """Waits for the element to be clickable, clicks and checks that there are no JS errors.
        """
        self.wait_for_element(by, selector, timeout=timeout, condition=EC.element_to_be_clickable).click()
        self.assert_no_javascript_error()

    def ajax_complete(self, driver):
        """Check if there are outstanding ajax calls.
        """
        try:
            return 0 == driver.execute_script("return jQuery.active")
        except:
            pass

    def wait_for_ajax_to_complete(self):
        """Waits until all ajax calls are completed.
        """
        WebDriverWait(self.driver, 10).until(self.ajax_complete, "")

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        """Waits until page is loaded.
        """
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(
            staleness_of(old_page)
        )

    def get_javascript_errors(self):
        """Checks if the javascript has created an error.
        """
        return self.wait_for_element(
            By.TAG_NAME, 'body').get_attribute('JSError')

    def assert_no_javascript_error(self):
        """Asserts that the there are no javascript errors.
        """
        self.assertIsNone(self.get_javascript_errors())

    def get_class_list(self, element) -> str:
        """
        Extracts the class list from the given element
        Args:
            element: The element to extract the class list from

        Returns:
            str: A string representing the class list concatenated with one whitespace
        """
        return element.get_attribute('class')

    def is_active(self, element) -> bool:
        """
        Checks if the given element has the class active
        Args:
            element: The element to check if it is active

        Returns:
            bool: True if active in class list, False else
        """
        return 'active' in self.get_class_list(element)
