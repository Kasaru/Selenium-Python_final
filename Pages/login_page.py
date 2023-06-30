from Pages.base_page import BasePage
from Pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in LoginPageLocators.LOGIN_URL, "Not login URL"
        assert True

    def should_be_login_form(self):
        assert LoginPageLocators.LOGIN_FORM, "Login form not found"
        assert LoginPageLocators.LOGIN_FIELD, "Login field not found"
        assert LoginPageLocators.PASSWD_LOG_FIELD, "Password field not found"
        assert LoginPageLocators.LOGIN_BUTTON, "Login button not found"
        assert True

    def should_be_register_form(self):
        assert LoginPageLocators.REGISTRATION_FORM, "Registration form not found"
        assert LoginPageLocators.REGISTRATION_EMAIL_FIELD, "Registration email field not found"
        assert LoginPageLocators.REGISTRATION_PASSWD_FIELD, "Registration password field not found"
        assert LoginPageLocators.REGISTRATION_REPEAT_PASSWD_FIELD, "Registration repeat password field not found"
        assert LoginPageLocators.REGISTRATION_BUTTON, "Registration button not found"
        assert True

    def register_new_user(self, email, password):
        print(f"email - {email}")
        print(f"password - {password}")
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWD_FIELD)
        pass_field.send_keys(password)
        rep_pass_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWD_FIELD)
        rep_pass_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
