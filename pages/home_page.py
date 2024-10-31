# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators for the navigation and Careers page sections
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")
    LOCATIONS_SECTION = (By.CSS_SELECTOR, ".career-location")
    TEAMS_SECTION = (By.CSS_SELECTOR, ".career-team")
    LIFE_AT_INSIDER_SECTION = (By.CSS_SELECTOR, ".life-at-insider")

    def open_company_menu(self):
        self.close_notifications_popup()  # Ensure popup is closed
        self.click(self.COMPANY_MENU)

    def go_to_careers(self):
        self.click(self.CAREERS_LINK)

    
