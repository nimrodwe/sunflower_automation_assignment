import allure
from playwright.sync_api import expect

@allure.epic("User Registration and Checkout")
@allure.feature("Checkout Flow")
@allure.story("Validate that selected product appears correctly in the shopping cart")
class TestCheckoutFlow:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify that a product selected after registration is in the checkout")
    def test_product_in_checkout(self, initialize):
        with allure.step("Open Register page"):
            initialize.header_section.click_register_header_btn()

        with allure.step("Select random gender"):
            initialize.register_page.select_random_gender()

        with allure.step("Fill personal details"):
            initialize.register_page.fill_first_name(initialize.first_name)
            initialize.register_page.fill_last_name(initialize.last_name)
            initialize.register_page.fill_email(initialize.email)

        with allure.step("Set password"):
            initialize.register_page.fill_password(initialize.password)
            initialize.register_page.fill_confirm_password(initialize.password)

        with allure.step("Submit registration"):
            initialize.register_page.submit_register()

        with allure.step("Click continue"):
            initialize.register_page.click_continue()

        with allure.step("Validate registration header"):
            expect(initialize.header_section.registered_user_link).to_be_visible()

        with allure.step("Navigate to Digital Downloads"):
            initialize.navbar_section.click_digital_downloads()

        with allure.step("Select a random product"):
            product_name = initialize.digital_downloads_page.click_random_product()

        with allure.step("Add product to cart"):
            initialize.product_page.click_cart_btn()
            initialize.product_page.wait_for_success_message()

        with allure.step("Go to Shopping Cart"):
            initialize.header_section.click_shopping_cart_header_btn()

        with allure.step("Verify product in checkout matches selected product"):
            assert product_name == initialize.checkout_page.get_product_name()
