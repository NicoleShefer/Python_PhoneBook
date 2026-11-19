from os import name

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ContactPage:
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='LastName']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='Description']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(., 'Save')]")
    ADD_CONTACT_BUTTON = (By.CSS_SELECTOR, "[HREF='/add']")

    def __init__(self, driver):
        self.driver = driver

    def open_contact_form(self):
        self.driver.find_element(*self.ADD_CONTACT_BUTTON).click()

    def fill_name_field(self):
        self.driver.find_element_by_css_selector(*self.NAME_INPUT).clear()
        self.driver.find_element_by_css_selector(*self.NAME_INPUT).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element_by_css_selector(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element_by_css_selector(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_phone(self, phone):
        self.driver.find_element_by_css_selector(*self.PHONE_INPUT).clear()
        self.driver.find_element_by_css_selector(*self.PHONE_INPUT).send_keys(phone)

    def fill_address(self, address):
        self.driver.find_element_by_css_selector(*self.ADDRESS_INPUT).clear()
        self.driver.find_element_by_css_selector(*self.NAME_INPUT).send_keys(address)

    def fill_description(self, description):
        self.driver.find_element_by_css_selector(*self.DESCRIPTION_INPUT).clear()
        self.driver.find_element_by_css_selector(*self.DESCRIPTION_INPUT).send_keys(description)

    def fill_contact(self, contact):
        self.driver.find_element_by_css_selector(*self.ADD_CONTACT_BUTTON).clear()
        self.driver.find_element_by_css_selector(*self.ADD_CONTACT_BUTTON).send_keys(contact)

    def submit_contact(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def contact_card_visible(self, phone):
        locator = (By.XPATH, f"//h3[contains(text(),'{phone}')]")
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))
        return element.is_displayed()

    def open_contact_details_card(self, phone, contact_page):
        card = self.driver.find_element(By.XPATH, f"//h3[contains(text(),'{phone}')]/..").click()










