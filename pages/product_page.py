from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def go_to_buy_book(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET)
        link.click()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET), "Button add to basket is not presented"

    def should_be_text_about_add_to_basket(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET), "Button add to basket is not presented"

    def product_name(self):
        return self.browser.find_element(*BasketPageLocators.NAME_OF_PRODUCT).text

    def product_price(self):
        return self.browser.find_element(*BasketPageLocators.PRICE_OF_PRODUCT).text

    def should_be_all_text_about_add_to_basket(self):
        self.text_add_to_basket(self.product_name())
        self.text_about_price(self.product_price())

    def text_add_to_basket(self, name):
        assert self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE), "Adding message isn't presented"
        text_add_to_basket = self.browser.find_element(*BasketPageLocators.SUCCESS_MESSAGE).text
        assert text_add_to_basket == f"{name} has been added to your basket.", \
            "Text about add book incorrect"

    def text_about_price(self, price):
        assert self.is_element_present(*BasketPageLocators.TEXT_ADD_TO_BASKET_PRICE), "Price message isn't presented"
        text_price_basket = self.browser.find_element(*BasketPageLocators.TEXT_ADD_TO_BASKET_PRICE).text
        assert text_price_basket == f"Your basket total is now {price}", \
            "Text about price book incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message should be disappeared, but isn't"

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")