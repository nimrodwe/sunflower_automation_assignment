import logging
import os
from dotenv import load_dotenv
from pages.header_section import HeaderSection
from pages.register_page import RegisterPage
from pages.navbar_section import NavbarSection
from pages.digital_downloads_page import DigitalDownloadsPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from faker import Faker


dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

faker = Faker()

class BaseClass:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.first_name = faker.first_name()
        self.last_name = faker.last_name()
        self.email = faker.unique.email()
        self.password = faker.password()
        self.header_section = HeaderSection(self.page)
        self.navbar_section = NavbarSection(self.page)
        self.digital_downloads_page = DigitalDownloadsPage(self.page)
        self.product_page = ProductPage(self.page)
        self.checkout_page = CheckoutPage(self.page)
        self.register_page = RegisterPage(self.page)
