# pages/careers_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):
    # Updated Locators for section headers using XPath for text matching
    LOCATIONS_HEADER = (By.XPATH, "//h3[contains(text(), 'Our Locations')]")  # Locator for "Our Locations"
    TEAMS_HEADER = (By.XPATH, "//h3[contains(text(), 'Find your calling')]")  # Locator for "Find Your Calling"
    LIFE_AT_INSIDER_HEADER = (By.XPATH, "//h2[contains(text(), 'Life at Insider')]")  # Locator for "Life at Insider"
    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all teams')]")
    QA_TITLE = (By.XPATH, "//h3[contains(text(),'Quality Assurance')]")

    def is_locations_visible(self):
        """Check if the 'Our Locations' section header is visible after scrolling."""
        self.scroll_to_element(self.LOCATIONS_HEADER)  # Scroll to the 'Our Locations' section header
        return self.find_element(self.LOCATIONS_HEADER).is_displayed()  # Return visibility status

    def is_teams_visible(self):
        """Check if the 'Find Your Calling' section header is visible after scrolling."""
        self.scroll_to_element(self.TEAMS_HEADER)  # Scroll to the 'Find Your Calling' section header
        return self.find_element(self.TEAMS_HEADER).is_displayed()  # Return visibility status

    def is_life_at_insider_visible(self):
        """Check if the 'Life at Insider' section header is visible after scrolling."""
        self.scroll_to_element(self.LIFE_AT_INSIDER_HEADER)  # Scroll to the 'Life at Insider' section header
        return self.find_element(self.LIFE_AT_INSIDER_HEADER).is_displayed()  # Return visibility status

    def click_see_all_teams(self):
        """Clicks on the 'See all teams' button."""
        self.scroll_to_element(self.SEE_ALL_TEAMS_BUTTON)
        self.click(self.SEE_ALL_TEAMS_BUTTON)

    def scroll_to_and_click_qa_title(self):
        """Scrolls to and clicks on the 'Quality Assurance' title."""
        self.scroll_to_element(self.QA_TITLE)
        self.click(self.QA_TITLE)
