"""
This module contains the page object for the sample app
"""

from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPage:
    url = 'http://uitestingplayground.com/sampleapp'

    # Text boxes
    username = (By.CSS_SELECTOR, 'input[name=UserName]')
    password = (By.CSS_SELECTOR, 'input[name=Password]')

    # Buttons
    log_in_button = (By.CSS_SELECTOR, 'button[id=login]')

    # Labels
    label_status = (By.CSS_SELECTOR, 'label[id=loginstatus]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def fill_in_username(self, username):
        username_input = self.browser.find_element(*self.username)
        username_input.send_keys(username)

    def fill_in_password(self, password):
        password_input = self.browser.find_element(*self.password)
        password_input.send_keys(password)

    def click_log_in(self):
        log_in_button = self.browser.find_element(*self.log_in_button)
        log_in_button.click()

    def get_label_status(self):
        label = self.browser.find_element(*self.label_status)
        return label

    def log_in(self, username, password):
        self.fill_in_username(username)
        self.fill_in_password(password)
        self.click_log_in()

    def log_out(self):
        self.click_log_in()


