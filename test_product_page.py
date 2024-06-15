import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_with_cost()
    page.should_be_message_added_to_basket()
    page.message_contains_name_of_the_book()
    page.cost_in_basket_equals_to_page()
    # time.sleep(80)
#div.alertinner/p/strong.text == p.price_color
