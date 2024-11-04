# pages/qa_jobs_page.py
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QAJobsPage(BasePage):
    SEE_ALL_QA_JOBS = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    LOCATION_OPTION = "Istanbul, Turkey"  
    LOCATION_DROPDOWN = (By.XPATH, "//label[contains(text(), 'Filter by Location')]//following-sibling::span")
    # LOCATION_DROPDOWN = (By.XPATH, "//select[@name='location']")
    # //label[contains(text(), 'Filter by Location')]//following-sibling::span
    # LOCATION_DROPDOWN = (By.CLASS_NAME, "select2-container")
    ISTANBUL_OPTION = (By.XPATH, f"//span[contains(@class, 'select2-results')]//li[contains(text(), '{LOCATION_OPTION}')]")
    # ISTANBUL_OPTION = (By.XPATH, "//span[contains(@class, 'select2-results')]//li[contains(text(), 'Istanbul, Turkey')]")
    # ISTANBUL_OPTION = (By.XPATH, "//option[text()='Istanbul, Turkey']")
    # Locator for the Filter by Department dropdown
    # DEPARTMENT_DROPDOWN = (By.ID, "department-filter")
    DEPARTMENT_DROPDOWN = (By.XPATH, "//label[contains(text(), 'Filter by Department')]//following-sibling::span")
    # DEPARTMENT_DROPDOWN = (By.CLASS_NAME, "select2-selection__arrow")
    # Locator for the Quality Assurance option
    QUALITY_ASSURANCE_OPTION = (By.XPATH, "//span[contains(@class, 'select2-results')]//li[contains(text(), 'Quality Assurance')]")
    # QUALITY_ASSURANCE_OPTION = (By.XPATH, "//option[text()='Quality Assurance']")
    JOB_LISTINGS = (By.CSS_SELECTOR, "//section[@id='career-position-list']//*[@data-location and @data-team]")
    # JOB_LISTINGS = (By.CSS_SELECTOR, ".position-list.col-12.d-flex.flex-wrap.mt-5.pl-2.pr-2.pl-lg-0.pr-lg-0.pt-4")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[text()='View Role']")
    POSITION_TITLE_SELECTOR = (By.CSS_SELECTOR, "p.position-title.font-weight-bold")
    


    def click_see_all_qa_jobs(self):
        self.click(self.SEE_ALL_QA_JOBS)

    def filter_location(self, location=LOCATION_OPTION):
        time.sleep(30)

        # Click to expand the dropdown
        self.click(self.LOCATION_DROPDOWN)
        # Build location option xpath
        locationXpath = f"//span[contains(@class, 'select2-results')]//li[contains(text(), '{location}')]"
        locationElement = (By.XPATH, locationXpath)
        # Select the location option
        self.click(locationElement)

    def filter_department(self, department="Quality Assurance"):
        # Click to expand the dropdown
        self.click(self.DEPARTMENT_DROPDOWN)
        # Select the department option
        self.click(self.QUALITY_ASSURANCE_OPTION)

    def get_job_listings(self):
        self.scroll_to_element(self.JOB_LISTINGS)
        return self.driver.find_elements(*self.JOB_LISTINGS)

    def hover_and_click_view_role(self, job_index):
        """Hover over the specified job listing and click the 'View Role' button."""
        job_listings = self.find_elements(*self.JOB_LISTINGS)
        if job_index < len(job_listings):
            action = ActionChains(self.driver)
            job_listing = job_listings[job_index]  # Get the specific job listing
        action = ActionChains(self.driver)
        # Hover over the job listing
        action.move_to_element(job_listing).perform()
        # Wait for the 'View Role' button to be present and then click
        view_role_button = job_listing.find_element(*self.VIEW_ROLE_BUTTON)
        view_role_button.click()
        
        # //section[@id='career-position-list']//*[@data-location and @data-team]
        # //section[@id='career-position-list']//div[./div[contains(text(), 'Istanbul, Turkey')] and ./span[contains(text(), 'Quality Assurance')]]
