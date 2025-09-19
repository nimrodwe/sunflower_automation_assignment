import logging
import allure
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Navbar Section Actions")
class NavbarSection(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.digital_downloads_link = page.get_by_role("link", name="Digital downloads").first


    def click_digital_downloads(self):
        self.click(self.digital_downloads_link)
        self.logger.info("Clicked digital downloads successfully")







