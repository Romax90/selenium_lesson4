import time

from .pages.main_page import MainPage
from .pages.product_page import ProductPage





def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page_product = ProductPage(browser, link)
    page_product.open()
    add_button = ProductPage(browser, browser.current_url)
    add_button.click_add_button()
    page_product.solve_quiz_and_get_code()
    time.sleep(5)
    page_product.should_be_add_to_card_message()
    page_product.should_be_name_product_must_match_name_product_add_to_card()
    page_product.should_be_a_price_message()
    page_product.should_be_price_product_must_match_price_product_add_to_card()
   # time.sleep(10)
