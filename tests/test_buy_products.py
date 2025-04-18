
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

import pages.login_page
import pages.catalog_page
import pages.product_page
import pages.cart_page
import pages.payment_page
import pages.finish_page
import pages.profile_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def test_buy_products(set_up):
    service = ChromeService(executable_path='C:\\Users\\Public\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    login = pages.login_page.Login_page(driver)
    login.authorization()

    catalog = pages.catalog_page.Catalog_page(driver)
    catalog.catalog_select_product()

    add_product = pages.product_page.Product_page(driver)
    add_product.add_product()

    cart = pages.cart_page.Cart_page(driver)
    cart.cart_input_user_data()

    payment_info = pages.payment_page.Payment_page(driver)
    payment_info.payment()

    cancel = pages.profile_page.Profile_page(driver)
    cancel.cancel_order()

    finish = pages.finish_page.Finish_page(driver)
    finish.get_screenshot()
