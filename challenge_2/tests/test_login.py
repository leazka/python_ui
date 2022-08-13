from challenge_2.pages import main_page


class TestLogin():
    def test_login_happy_path(self, browser):
        username = "name"
        password = "pwd"

        # Load the login page
        page = main_page.MainPage(browser)
        page.load()

        # Log in
        page.log_in(username, password)

        # Get label with resulting message
        label = page.get_label_status()

        expected_text = "Welcome, " + username + "!"
        assert label.text == expected_text

    def test_login_empty_username(self, browser):
        password = "pwd"

        # Load the login page
        page = main_page.MainPage(browser)
        page.load()

        # Fill in password and click login button
        page.fill_in_password(password)
        page.click_log_in()

        # Get label with resulting message
        label = page.get_label_status()

        expected_text = "Invalid username/password"
        assert label.text == expected_text

    def test_login_empty_password(self, browser):
        username = "username"

        # Load the login page
        page = main_page.MainPage(browser)
        page.load()

        # Fill in username and click login button
        page.fill_in_username(username)
        page.click_log_in()

        # Get label with resulting message
        label = page.get_label_status()

        expected_text = "Invalid username/password"
        assert label.text == expected_text

    def test_login_incorrect_password(self, browser):
        username = "username"
        password = "username"

        # Load the login page
        page = main_page.MainPage(browser)
        page.load()

        # Log in
        page.log_in(username, password)

        # Get label with resulting message
        label = page.get_label_status()

        expected_text = "Invalid username/password"
        assert label.text == expected_text
