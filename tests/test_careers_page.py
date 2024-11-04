# tests/test_careers_page.py
import unittest
import os
from utils.driver_factory import get_driver
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCareersPage(unittest.TestCase):
    HOME_PAGE_URL = "https://useinsider.com/"
    @classmethod
    def setUpClass(cls):
        cls.browser = os.getenv("BROWSER", "chrome").lower()  # Defaults to Chrome
        cls.driver = get_driver(cls.browser)
        cls.driver.implicitly_wait(10)
        cls.base_page = BasePage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.careers_page = CareersPage(cls.driver)
        cls.qa_jobs_page = QAJobsPage(cls.driver)

    def test_careers_page(self):
        try:

            # Step 1: Visit the Home page

            self.base_page.visit(self.HOME_PAGE_URL)

            self.base_page.wait_for_page_to_load()

            self.assertIn("Insider", self.driver.title, "Home page not opened correctly")

            self.home_page.close_cookie_banner()  # Close the cookie banner


            # Step 2: Navigate to Careers page

            self.home_page.open_company_menu()

            self.home_page.go_to_careers()
            
            self.base_page.wait_for_page_to_load()
            self.assertTrue(self.careers_page.is_teams_visible(), "Teams not visible")
            self.assertTrue(self.careers_page.is_locations_visible(), "Locations not visible")
            self.assertTrue(self.careers_page.is_life_at_insider_visible(), "Life at Insider not visible")



            # Step 3: Go to QA jobs, apply filters

            # Click "See all teams" and scroll to "Quality Assurance"
            self.careers_page.click_see_all_teams()
            
            self.careers_page.scroll_to_and_click_qa_title()
            self.base_page.wait_for_page_to_load()
            self.qa_jobs_page.click_see_all_qa_jobs()
            self.base_page.wait_for_page_to_load()
            self.qa_jobs_page.filter_location()

            self.qa_jobs_page.filter_department("Quality Assurance")

            jobs = self.qa_jobs_page.get_job_listings()
            # Wait for the job listings to be visible
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".position-list .position-title.font-weight-bold")))
            self.assertGreater(len(jobs), 0, "No QA jobs found for Istanbul, Turkey")



            # Step 4: Verify jobs

            for job in jobs:
                position = job.find_element(*QAJobsPage.POSITION_TITLE_SELECTOR).text
                department = job.find_element(By.CSS_SELECTOR, ".position-department").text
                location = job.find_element(By.CSS_SELECTOR, ".position-location").text

                # self.assertIn("Quality Assurance", position, "Job position does not match")
                self.assertIn("Quality Assurance", position, "Job position must include 'Quality Assurance'")

                self.assertIn("Quality Assurance", department, "Job department does not match")
                self.assertIn("Istanbul, Turkey", location, "Job location does not match")


            # Step 5: View role and verify redirection

            self.qa_jobs_page.hover_and_click_view_role()
            self.base_page.wait_for_page_to_load()
            self.assertIn("lever.co", self.driver.current_url, "Not redirected to Lever application")
        except AssertionError as e:
            self.take_screenshot("test_failure.png")  # Capture screenshot on failure
            raise e

    def take_screenshot(self, name):
        """Takes a screenshot with the specified filename."""
        self.driver.save_screenshot(name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
