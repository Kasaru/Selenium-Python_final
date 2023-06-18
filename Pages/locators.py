from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FIELD = (By.NAME, "login-username")
    PASSWD_LOG_FIELD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTRATION_PASSWD_FIELD = (By.NAME, "registration-password1")
    REGISTRATION_REPEAT_PASSWD_FIELD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
