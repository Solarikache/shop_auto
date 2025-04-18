import time
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Catalog_page(Base):

    url = 'https://malik-brand.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #рандом для выбора индекса
    random_index = random.randint(7, 10)

    #locators (локаторы)
    catalog_button = "//li[@id='menu-item-405']"
    filter_stock = "//a[@href = 'https://malik-brand.com/ru/shop/?filter_stock_status=instock']"
    filter_size = "//a[@href = 'https://malik-brand.com/ru/shop/?filter_stock_status=instock&filter_size=42-44']"
    hover_element = f"(//div[@class='product_card__name'])[7]"
    product = f"(//a[@class='add_to_cart product_card__button'])[7]"

    #getters (получаем информацию об элементе)

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_filter_stock(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_stock)))

    def get_filter_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size)))

    def get_hover_element(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.hover_element)))

    def get_selected_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_filter_stock(self):
        self.get_filter_stock().click()
        print("Click stock filter")

    def click_filter_size(self):
        self.get_filter_size().click()
        print("Click size filter")

    def move_hover_element(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_hover_element()).perform()
        time.sleep(1)
        print("Move to element price")

    def click_selected_product(self):
        self.get_selected_product().click()
        time.sleep(3)
        print("Click product in catalog, go product")

    #metods (методы)

    def catalog_select_product(self):
        self.get_current_url()
        self.click_catalog_button()
        self.click_filter_stock()
        self.click_filter_size()
        self.move_hover_element()
        self.click_selected_product()
