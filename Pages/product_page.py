#pytest -v -s --tb=line --language=en test_product_page.py
from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_same_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE)
        assert message.text == f"{name.text} был добавлен в вашу корзину.", "message is not equal"

    def should_be_same_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_price = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_PRICE_MESSAGE)
        assert price.text == message_price.text, "price is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented, but should be"
