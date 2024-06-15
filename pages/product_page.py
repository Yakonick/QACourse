from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_message_with_cost(self):
        assert self.is_element_present(*ProductPageLocators.COST_IN_BASKET), "There is no message with cost in basket"

    def should_be_message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_NAME_OF_BOOK), \
            "There is no message on the page"

    def message_contains_name_of_the_book(self):
        name_of_the_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_NAME_OF_BOOK).text
        assert name_of_the_book == name_in_message, "Name of the book in the message is different to original one"

    def cost_in_basket_equals_to_page(self):
        cost_in_basket = self.browser.find_element(*ProductPageLocators.COST_IN_BASKET).text
        cost_in_page = self.browser.find_element(*ProductPageLocators.COST_IN_PAGE).text
        assert cost_in_basket == cost_in_page, "Different costs"

    def cannot_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_WITH_NAME_OF_BOOK), "is present"

    def dissapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_WITH_NAME_OF_BOOK), "Not dissapeared element"
