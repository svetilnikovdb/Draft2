import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

class PythonSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
        time.sleep(2)

    def test_title(self):
        self.assertEqual(self.driver.title, "Welcome to Python.org")

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
