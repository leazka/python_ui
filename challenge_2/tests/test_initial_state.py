from challenge_2.pages import main_page


class TestInitialState():
    def test_initial_state(self, browser):
        # Load the login page
        page = main_page.MainPage(browser)
        page.load()

        # Get label
        label = page.get_label_status()

        expected_text = "User logged out."
        assert label.text == expected_text
