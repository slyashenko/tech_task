# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators for the navigation and Careers page sections
    COMPANY_MENU = (By.XPATH, "//*[@id='navbarDropdownMenuLink' and contains(., 'Company')]")
    CAREERS_LINK = (By.XPATH, "//*[@id='navbarDropdownMenuLink' and contains(., 'Company')]/following-sibling::div//a[text()='Careers']")
   
    def open_company_menu(self):
        self.close_notifications_popup()  # Ensure popup is closed
        self.click(self.COMPANY_MENU)

    def go_to_careers(self):
        self.click(self.CAREERS_LINK)

    
