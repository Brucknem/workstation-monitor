import sys
import unittest
from tests.frontend.ui_tests_base import UITestsBase
from src.frontend.app import app
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasicUITests(UITestsBase):
    """Basic UI tests.
    Opening the index and about pages, transitioning between these.
    """

    def test_index(self):
        """Tests opening the index page
        """
        element = self.driver.find_element(By.ID, "navbar-brand")
        inner_html = element.get_attribute('innerHTML')
        self.assertEqual("Workstation", inner_html)


    def test_about(self):
        """Tests opening the about page
        """
        self.driver.get("http://127.0.0.1:5000/about")
        self.assertEqual("Workstation Monitor - About", self.driver.title)

    def test_index_about_transition(self):
        """Tests transitioning from index to about and back
        """
        self.driver.get("http://127.0.0.1:5000/")

        self.assertEqual("Workstation Monitor", self.driver.title)        

        with self.wait_for_page_load(timeout=2):
            self.click_element(By.LINK_TEXT, 'About')
        self.assertEqual("Workstation Monitor - About", self.driver.title)

        with self.wait_for_page_load(timeout=2):
            self.click_element(By.LINK_TEXT, 'Workstation')
        self.wait_for_element(By.CLASS_NAME, 'h2')
        self.assertEqual("Workstation Monitor", self.driver.title)        

if __name__ == "__main__":
    unittest.main()
