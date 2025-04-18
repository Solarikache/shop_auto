import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Payment_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    delivery_type = "(//label[@class='sc-dPiJTX jRjKRm'])[2]"
    input_address = "//input[@id = 'adress']"
    city = "(//li[@class = 'sc-AjnNk iFUekl'])[2]"
    payment_type = "(//label[@class = 'sc-cTAoTO fgfQvd'])[1]"
    submit_information_button = "//button[@class = 'sc-egifa hDIjGz']"

    #Getters
    def get_delivery_type(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.delivery_type)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_address)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_payment_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_type)))

    def get_submit_info_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_information_button)))

    #Actions
    def select_delivery_type(self):
        self.get_delivery_type().click()
        print("Select delivery type")

    def input_city(self):
        self.get_address().click()
        self.get_address().send_keys("Чел")
        self.driver.execute_script("window.scrollTo(0, 200);")
        print("Click address field and input")

    def select_city(self):
        self.get_city().click()
        print("Select city")

    def select_payment_type(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Scroll down")
        time.sleep(3)
        self.get_payment_type().click()
        print("Select payment type")

    def click_submit_button(self):
        self.get_submit_info_button().click()
        print("Click submit button")
        time.sleep(15)

    #Methods
    def payment(self):
        self.get_current_url()
        self.select_delivery_type()
        self.input_city()
        self.select_city()
        self.select_payment_type()
        # self.click_submit_button()