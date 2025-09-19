import logging
import allure
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Product Page Actions")
class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.cart_button = page.locator("input.button-1.add-to-cart-button[value='Add to cart']")
        self.add_to_cart_success_message = page.locator('p.content', has_text="The product has been added to your")

    def click_cart_btn(self):
        self.click(self.cart_button)
        self.logger.info("Clicked cart button successfully")

    def wait_for_success_message(self):
        self.wait_for_element(self.add_to_cart_success_message)
        self.logger.info("Product successfully added to cart")

