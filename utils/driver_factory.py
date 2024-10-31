# utils/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # Disable notifications in Chrome

        chrome_prefs = {"profile.default_content_setting_values.notifications": 2}

        chrome_options.add_experimental_option("prefs", chrome_prefs)
        
        # Set up Chrome driver with Service
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    elif browser_name.lower() == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        # Disable notifications in Firefox

        firefox_options.set_preference("dom.webnotifications.enabled", False)
        
        # Set up Firefox driver with Service
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        return driver

    else:
        raise ValueError("Unsupported browser! Choose 'chrome' or 'firefox'")
