import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    #Metod get current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Сurrent url " + get_url)

    #Metod assert world in all list
    def assert_word_in_profile(self, word, result):
        value_word = word.text
        assert value_word == result
        print("PASS. Authorization complete")

    def assert_word_in_cart(self, word, result):
        value_word = word.text
        assert value_word == result
        print("PASS. Cart is open")

    def assert_product_name(self, product_name,result):
        value_product_name = product_name.text
        assert value_product_name == result
        print("PASS. Product is valid: " + product_name)

    def assert_cancel_order_text(self, message, result):
        value_message = message.text
        assert value_message == result
        print("PASS. Order cancel success")

    #Method screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\Public\\Malik_ecom\\screen\\' + name_screenshot)

    # Method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("PASS. URL is correct")

    def assert_url_contains(self, expected_part):
        current_url = self.driver.current_url
        assert expected_part in current_url, f"URL не содержит '{expected_part}'. Актуальный URL: {current_url}"
        return True

    def scroll_down_300(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Scroll down")

    def assert_cart_success_message(self, message, result):
        value_cart_message = message.text
        assert result in value_cart_message, f"Ожидался текст '{result}', получено '{value_cart_message}'"
        print("PASS. Product add to cart")
