
class LoginPage:
    def __init__(self, page):
        self.page = page

        self.url = "https://www.saucedemo.com/"

        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """return error message if it appears"""
        return self.error_message.inner_text()

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.url)
