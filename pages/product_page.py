import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.catalog_page import Catalog_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Product_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    product_size = "//label[contains(text(), '42-44')]"
    cart_button = "//button[@id='add_to_cart_button__malik']"
    # product_color = "//span[@class = 'label_color']"
    cart_success_message = "//a[contains(text(), 'Просмотр корзины')]"

    #Getters
    def get_select_product_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_size)))

    # def get_product_color(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_color)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cart_success_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_success_message)))

    #Actions
    def click_product_size(self):
        time.sleep(2)
        self.get_select_product_size().click()
        print("Select product size")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    #Methods
    def add_product(self):
        self.get_current_url()
        self.click_product_size()
        self.click_cart_button()
        self.assert_cart_success_message(self.get_cart_success_message(), "ПРОСМОТР КОРЗИНЫ")
