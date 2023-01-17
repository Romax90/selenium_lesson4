from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
   # LOGIN_URL = browser.current_url
    LOGIN_FORM = (By.ID, "login_form")
    REGISTED_FORM = (By.ID, "register_form")

