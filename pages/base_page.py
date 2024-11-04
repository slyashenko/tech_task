# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # Import ActionChains

class BasePage:
    HOME_PAGE_URL = "https://useinsider.com/"
    NOTIFICATIONS_POPUP = (By.CSS_SELECTOR, ".insider-push-close-button")
    DECLINE_ALL_COOKIES = (By.XPATH, "//a[@id='wt-cli-reject-btn' and text()='Decline All']")
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def visit(self, url):
        self.driver.get(url)

    def wait_for_page_to_load(self, timeout=10):
        """Wait until the page is fully loaded."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def close_notifications_popup(self):
        try:
            # Update the locator to match the "No Thanks" or "Close" button in the popup
            popup_close_button = self.driver.find_element(*self.NOTIFICATIONS_POPUP)
            popup_close_button.click()
        except NoSuchElementException:
            pass  # Popup is not present, so continue with the test

    def close_cookie_banner(self):
        try:
            # Locate the "Accept All" button for cookies
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DECLINE_ALL_COOKIES)
                # EC.element_to_be_clickable((By.CSS_SELECTOR, "a#wt-cli-accept-all-btn"))
            )
            cookie_button.click()  # Click the button to close the cookie banner
        except TimeoutException:
            pass  # Ignore if banner isn't present or already closed    

    def find_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        """Scrolls to the specified element using ActionChains."""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()  # Move to the element
        # Optionally wait for the element to be visible after scrolling
        WebDriverWait(self.driver, 15).until(EC.visibility_of(element))            
    

    def click(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        element.click()

    def is_element_visible(self, locator, timeout=10):
        """Check if an element is visible within a given timeout."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    
    def take_screenshot(self, name="screenshot.png"):
        self.driver.save_screenshot(name)
