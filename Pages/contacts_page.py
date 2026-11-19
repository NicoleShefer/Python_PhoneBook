import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage

class ContactsPage(BasePage):
    CONTACTS_LINK = (By.CSS_SELECTOR, "[href='/contacts']")
    CONTACTS_CARDS = (By.CLASS_NAME, "contact-item_card__2SOIM")
    EDIT_BUTTON = (By.XPATH, "//button[text()='Edit']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='desc']")

    def open_contact_list(self):
        self.click(self.CONTACTS_LINK)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/contacts"))
        time.sleep(1)

    def get_contact_card(self, phone):
        return self.find(f"//h3[text()='{phone}']")

    def contact_cards_visible(self, phone):
        locator = self.get_card_locator(phone)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return element.is_displayed()

    def open_contact_details_card(self, phone):
        self.click(self.get_card_locator(phone))

    @staticmethod
    def get_card_locator(phone):
        return By.XPATH, f"//h3[contains(text(), '{phone}')]"

    def open_edit_contact_mode(self):
        self.click(self.EDIT_BUTTON)

    def set_edit_mode(self, locator, value):
        self.fill(locator, value)

    def submit_edit(self):
        self.click(self.SAVE_BUTTON)
        time.sleep(1)