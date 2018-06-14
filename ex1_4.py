# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class Exercise(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_open(self):
    self.driver.maximize_window()
    self.driver.get('http://wsb.pl/wroclaw/')

    #self.driver.implicitly_wait(5)
    logo=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'logo')))

    element=self.driver.find_element_by_id('edit-search-block-form--2')
    element.send_keys('tester')
    #time.sleep(5)
    element.send_keys(Keys.ENTER)
    title=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'page-title')))
    #time.sleep(10)
    results=self.driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/ol/li')
    print('Znalazlam '+str(len(results))+' wynikow')
    for i in results:
        print(i.text + '\n')
    self.assertEqual(12, len(results))


    #element.send_keys(u'\ue007')

  def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
