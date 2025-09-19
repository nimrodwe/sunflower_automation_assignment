import logging
import random
import allure
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Digital Downloads Page Actions")
class DigitalDownloadsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.all_product_links = page.locator("h2.product-title > a")

    def click_random_product(self):
        links = self.all_product_links.all()
        random_link = random.choice(links)
        product_name = random_link.inner_text()
        random_link.click()
        self.logger.info(f"Clicked a random product called '{product_name}' successfully")
        return product_name
