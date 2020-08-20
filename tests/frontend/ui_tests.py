import sys
import unittest
from src.frontend.app import app
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UiTests(unittest.TestCase):
    """UI tests.
    """

    def setUp(self):
        """Setup
        """
        self.server = Process(target=app.run, kwargs={'debug':True, 'use_debugger':True, 'threaded':False, 'use_reloader': False})
        self.server.start()
        self.driver = webdriver.Firefox()

    def tearDown(self):
        """Teardown
        """
        self.driver.get("http://127.0.0.1:5000/shutdown")
        self.driver.close()
        self.server.terminate()
        self.server.join()

    def test_index(self):
        """Tests opening the index page
        """
        self.driver.get("http://127.0.0.1:5000/")
        self.assertEqual("Workstation Monitor", self.driver.title)

        element = self.driver.find_element_by_id("navbar-brand")
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
        self.driver.find_element_by_link_text('About').click()

        self.assertEqual("Workstation Monitor - About", self.driver.title)
        self.driver.find_element_by_link_text('Workstation').click()

        self.assertEqual("Workstation Monitor", self.driver.title)        

if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
