from challenge_2.pages import main_page


class TestLogout():
    def test_logout_happy_path(self, browser):
        username = "name"
        password = "pwd"

        # Load the login page
        page = main_page.MainPage(browser)
        page.load()

        # Log in
        page.log_in(username, password)

        # Log out
        page.click_log_in()

        # Get label with resulting message
        label = page.get_label_status()

        expected_text = "User logged out."
        assert label.text == expected_text
