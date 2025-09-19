import logging
import random
from faker import Faker
import allure
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Fill Registration Form")
class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.male_radio = page.get_by_role("radio", name="Male", exact=True)
        self.female_radio = page.get_by_role("radio", name="Female", exact=True)
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password:", exact=True)
        self.confirm_password_input = page.get_by_role("textbox", name="Confirm password:", exact=True)
        self.register_btn = page.get_by_role("button", name="Register")
        self.continue_btn = page.get_by_role("button", name="Continue")
        self.email_exists_error = page.locator("div.validation-summary-errors li", has_text="already exists")

    def select_random_gender(self):
        gender_choice = random.choice(["M", "F"])
        if gender_choice == "M":
            self.wait_for_element(self.male_radio)
            self.male_radio.check()
            self.logger.info("Male gender selected")
        else:
            self.wait_for_element(self.female_radio)
            self.female_radio.check()
            self.logger.info("Female gender selected")

    def fill_first_name(self, first_name: str):
        self.clear_and_type(self.first_name_input, first_name)
        self.logger.info(f"First name '{first_name}' filled successfully")

    def fill_last_name(self, last_name: str):
        self.clear_and_type(self.last_name_input, last_name)
        self.logger.info(f"Last name '{last_name}' filled successfully")

    def fill_email(self, email: str):
        self.clear_and_type(self.email_input, email)
        self.logger.info(f"Email '{email}' filled successfully")

    def fill_password(self, password: str):
        self.clear_and_type(self.password_input, password)
        self.logger.info("Password filled successfully")

    def fill_confirm_password(self, confirm_password: str):
        self.clear_and_type(self.confirm_password_input, confirm_password)
        self.logger.info("Confirm password filled successfully")

    def click_continue(self):
        self.continue_btn.click()
        self.logger.info("Continue clicked successfully")

    def submit_register(self):
        self.register_btn.click()
        self.logger.info("Register button clicked successfully")

        # If the user registers with an existing email, generate a new one
        if self.email_exists_error.is_visible():
            new_email = Faker.unique.email()
            self.clear_and_type(self.email_input, new_email)
            self.logger.info(f"Email already exists, new email '{new_email}' filled")
            return new_email
        return None
