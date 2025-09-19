import logging
from playwright.sync_api import Page, Locator

# base page which contains common used functions

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, element: Locator):
        self.logger.debug(f"Clicking {element}")
        element.click()

    def type(self, element: Locator, text: str):
        self.logger.debug(f"Typing into element: {element}")
        element.type(text)

    def clear_and_type(self, element: Locator, text: str):
        element.clear()
        self.logger.debug(f"Clearing element: {element}")
        element.type(text)
        self.logger.debug(f"Typed text: {text}")

    def fill(self, element: Locator, text: str):
        self.logger.debug(f"Filling element: {element}, text: {text}")
        element.fill(text)

    def wait_for_element(self, element: Locator, timeout: int = 5000):
        self.logger.debug(f"Waiting for element: {element}")
        element.wait_for(state="visible", timeout=timeout)