import logging
import allure
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Header Section Actions")
class HeaderSection(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.register_btn_locator = page.get_by_role("link", name="Register")
        self.shopping_cart_locator = page.get_by_role("link", name="Shopping cart", exact=True)

    def click_register_header_btn(self):
        self.click(self.register_btn_locator)
        self.logger.info("Clicked register header button successfully")

    def click_shopping_cart_header_btn(self):
        self.click(self.shopping_cart_locator)
        self.logger.info("Clicked shopping cart header button successfully")

