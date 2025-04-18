import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Login_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    banner_exit = "(//div[@class='close'])[1]"
    user_menu = "//div[@class ='user_btn']"
    username = "//input[@id ='username']"
    password = "//input[@id ='password']"
    login_button = "//button[@class='btn']"
    profile_word = "//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--dashboard is-active']"

    #Getters

    def get_banner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.banner_exit)))

    def get_user_menu(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.user_menu)))

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_profile_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_word)))

    #Actions

    def close_banner(self):
        time.sleep(5)
        self.get_banner().click()
        print("Click close banner button")

    def click_user_menu(self):
        self.get_user_menu().click()
        print("Click user menu")

    def input_username(self, username):
        self.get_username().click()
        self.get_username().send_keys(username)
        print("Input email/username")

    def input_password(self, password):
        self.get_password().click()
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    #Metods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_user_menu()
        self.close_banner()
        self.input_username("6oq6e@ptct.net")
        self.input_password("test_2025!")
        self.click_login_button()
        self.assert_word_in_profile(self.get_profile_word(),"Панель управления")

