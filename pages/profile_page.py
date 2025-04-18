from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Profile_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    profile_button ="//div[@class = 'user_btn']"
    list_orders_button ="//li[@class = 'woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--orders']"
    cancel_order_button ="(//a[@class = 'woocommerce-button button cancel'])[1]"
    cancel_message = "//div[@class = 'woocommerce-info']"

    #Getters
    def get_profile_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_button)))

    def get_list_orders_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.list_orders_button)))

    def get_cancel_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_order_button)))

    def get_cancel_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_message)))

    #Actions
    def click_profile_button(self):
        self.get_profile_button().click()
        print("Click profile button")

    def click_list_orders_button(self):
        self.get_list_orders_button().click()
        print("Click list order button")

    def click_cancel_order_button(self):
        self.get_cancel_order_button().click()
        print("Click cancel order button")


    #Methods
    def cancel_order(self):
        self.driver.back()
        self.get_current_url()
        self.click_profile_button()
        self.click_list_orders_button()
        self.click_cancel_order_button()
        self.assert_cancel_order_text(self.cancel_message, "Ваш заказ отменен.")
