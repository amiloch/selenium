# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Exercise(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_open(self):
    self.driver.maximize_window()
    self.driver.get('https:\\wsb.pl')
    logo=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'logo')))
    #self.driver.implicitly_wait(5)
    self.assertIn(u'Uczelnie wyższe', self.driver.title)

  def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
