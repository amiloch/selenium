import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import epected_conditions as EC
import time

class Exercise(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_open(self):
    self.driver.maximize_window()
    self.driver.get('https:\\google.com')
    self.driver.implicitly_wait(5)
    self.assertIn('Buuu', self.driver.title)

  def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
