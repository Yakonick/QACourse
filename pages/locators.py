from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(@class, btn-default) and contains(@href, 'basket')]")


class BasketPageLocators:
    ITEM_IN_BASKET = (By.ID, "basket_fromset")
    BASKET_EMPTY_TEXT = (By.XPATH, "//div[@id='content_inner']/p")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    COST_IN_BASKET = (By.XPATH, "//strong[contains(text(), '£')]")
    COST_IN_PAGE = (By.XPATH, "//p[@class='price_color']")
    MESSAGE_WITH_NAME_OF_BOOK = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    NAME_OF_BOOK = (By.XPATH, "//h1")
