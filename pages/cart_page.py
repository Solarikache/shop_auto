from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Cart_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    product_name =" //div[@class = 'sc-hiwQrr gKOTyc']"
    cart_word = "//a[@href='/ru/cart/']"
    cart_button = "//div[@class='cart_label']"
    cart_success_button = "(//button[@class = 'sc-egifa hDIjGz'])[2]"
    user_info_success_button = "//button[@class='sc-egifa hDIjGz']"

    #Getters
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.product_name)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_cart_success_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_success_button)))

    def get_user_info_success_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_info_success_button)))

    #Actions
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def click_cart_success_button(self):
        self.get_cart_success_button().click()
        print("Click cart success button")

    def click_user_info_success_button(self):
        self.get_user_info_success_button().click()
        print("Click user info success button")

    #Methods
    def cart_input_user_data(self):
        self.get_current_url()
        self.click_cart_button()
        self.assert_word_in_cart(self.get_cart_word(), "Корзина")
        self.click_cart_success_button()
        self.click_user_info_success_button()

