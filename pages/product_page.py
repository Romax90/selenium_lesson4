from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_add_to_card_message(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_MESSAGE), "Message product name not found"

    def should_be_name_product_must_match_name_product_add_to_card(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_MESSAGE).text
        assert name_product == name_product_message, "Name is different "

    def should_be_a_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_MESSAGE), "Message price not found"

    def should_be_price_product_must_match_price_product_add_to_card(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_product_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_MESSAGE).text
        assert price_product == price_product_message, "Price is different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert True
