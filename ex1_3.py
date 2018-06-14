# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://wsb.pl/wroclaw/')
element=driver.find_element_by_id('edit-search-block-form--2').send_keys('tester')
time.sleep(5)
driver.quit()
