from Pages.locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.CART_BUTTON)
        link.click()
    def cart_should_not_contain_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_CART), "Cart contains products"
    def should_be_empty_cart_messge(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART), "Empty cart message is not presented, but should be"