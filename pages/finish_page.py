import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Finish_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators


    #Getters

    #Actions


    #Methods
    def payment(self):
        self.get_current_url()
        self.assert_url_contains("https://qr.nspk.ru/")
        self.get_screenshot()
