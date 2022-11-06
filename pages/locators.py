from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")

class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div.content p")
    BASKET_ITEMS_LIST = (By.CSS_SELECTOR, "div.content form#basket_formset")
'''
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
'''

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success")