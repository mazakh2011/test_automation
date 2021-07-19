from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.XPATH, "(//*[contains(@class, 'btn')])[3]/a")
    USER_ICON = (By.XPATH, "//*[@class='icon-user']")
	
class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//*[@name='login_submit']")
    REGISTER_BUTTON = (By.XPATH, "//*[@name='registration_submit']")
    EMAIL = (By.XPATH, "//*[@name='registration-email']")
    PASSWORD = (By.XPATH, "//*[@name='registration-password1']")
    CONFIRM_PASSWORD = (By.XPATH, "//*[@name='registration-password2']")
    USER_ICON = (By.XPATH, "//*[@class='icon-user']")
	
class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.XPATH, "(//*[contains(@class, 'content')])//p")
    ADD_TO_BASKET = (By.XPATH, "//*[contains(@class, 'btn-add-to-basket')]")
    NAME_OF_PRODUCT = (By.XPATH, "(//*[contains(@class, 'product_main')])/h1")
    PRICE_OF_PRODUCT = (By.XPATH, "(//*[contains(@class, 'price_color')])[2]")
    SUCCESS_MESSAGE = (By.XPATH, "(//*[contains(@class, 'alertinner')])[1]")
    TEXT_ADD_TO_BASKET_PRICE = (By.XPATH, "(//*[contains(@class, 'alertinner')])[3]//p[1]")