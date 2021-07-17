from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket should be empty"

        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert message == "Your basket is empty. Continue shopping", \
            "Message about empty basket incorrect"