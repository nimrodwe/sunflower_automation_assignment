import logging
import os
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
import pytest
from tests.base_class import BaseClass

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

@pytest.fixture(scope="function")
def initialize(request):
    headless_mode = os.getenv("DOCKER", "false").lower() == "true"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            args=["--start-maximized", "--disable-blink-features=AutomationControlled"],
            headless=headless_mode,
        )
        context = browser.new_context(
            locale="en-US",
            no_viewport=True,
        )

        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        base = BaseClass(page)
        page.goto(base.base_url)
        yield base


        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_dir = "../screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
            with open(screenshot_path, "wb") as f:
                f.write(page.screenshot(path=screenshot_path, full_page=True))
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="screenshot", attachment_type=AttachmentType.PNG)

        page.close()
        context.close()


