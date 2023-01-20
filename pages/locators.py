from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
   # LOGIN_URL = browser.current_url
    LOGIN_FORM = (By.ID, "login_form")
    REGISTED_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')

    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    NAME_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    PRICE_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')

    FILD_ADD_TO_BAG = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    FILD_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')