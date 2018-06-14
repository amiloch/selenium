# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from faker import Faker
import random
from selenium.webdriver.support.ui import Select

class WizzAir(unittest.TestCase):

    fake = Faker('ar_EG')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl#/')
        time.sleep(5)

    def test_register(self):

        log=self.driver.find_element_by_css_selector('#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button')
        log.click()
        self.driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button').click()
        time.sleep(3)
        first_name=self.driver.find_element_by_xpath("//input[@placeholder='Imię']").send_keys(self.fake.first_name())
        last_name=self.driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-1"]/label[2]/div[1]/input').send_keys(self.fake.last_name())
        fem=self.driver.find_element_by_id('register-gender-male')
        fem.click()
        phone=self.driver.find_element_by_xpath("//input[@placeholder='Telefon komórkowy']").send_keys(self.fake.msisdn())
        mail=self.driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[1]/label/input').send_keys('blablablagmail.com')
        password=self.driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-5"]/div[1]/label/input').send_keys('KuKuryku00')
        country=self.driver.find_element_by_xpath("//input[@placeholder='Obywatelstwo']").click()
        country_choose=self.driver.find_element_by_xpath('//*[@class="register-form__country-container__locations"]/label[164]')
        country_choose.location_once_scrolled_into_view
        country_choose.click()
        #box1=self.driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[9]/span/label[1]').click()
        boxes=self.driver.find_elements_by_xpath('//label[@for="registration-special-offers-checkbox"]')[1].click()
        box2=self.driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[10]/span/label[1]').click()
        #boxes.self.get(1).click()
        error_message=self.driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span')
        print(error_message.text)
        assert error_message.is_displayed()
        self.assertEqual(error_message.text, u'Nieprawidłowy adres e-mail')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
