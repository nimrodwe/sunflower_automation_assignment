import logging
import allure
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Checkout Page Actions")
class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.product_name_checkout_locator = page.locator("td.product > a")

    def get_product_name(self):
        self.logger.info("Getting product name")
        return self.product_name_checkout_locator.inner_text()


