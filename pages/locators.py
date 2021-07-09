from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//*[@name='login_submit']")
    REGISTER_BUTTON = (By.XPATH, "//*[@name='registration_submit']")
	