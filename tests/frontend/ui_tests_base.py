import sys
import unittest
from src.frontend.app import app
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UITestsBase(unittest.TestCase):
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