from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_add_to_basket_button()
        
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not presented"
        
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"
    
    def add_to_basket_click(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_product_name_message(self):
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name_message.text == product_name.text, \
            "Product name in message is not the same that product name on page"

    def should_be_correct_product_price_message(self):
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price_message.text == product_price.text, \
            "Product price in message is not the same that product price on page"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should disappear"
