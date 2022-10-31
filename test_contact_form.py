import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ContactFormTest(unittest.TestCase):
    LINK = "https://unicreds.com/contact-us"

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self) -> None:
        self.driver.quit()

    def test_contact_submission(self):
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "fullname").send_keys("Test Automation")
        self.driver.find_element(By.NAME, "email").send_keys("test@yopmail.com")
        self.driver.find_element(By.ID, "phone").send_keys("0101010101")
        self.driver.find_element(By.ID, "message").send_keys("Testing")
        self.driver.find_element(By.ID, "contactButton").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'formMessage'), "Message sent successfully!"))

    def test_invalid_form_inputs(self):
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "email").send_keys("test.com")
        self.driver.find_element(By.ID, "phone").send_keys("01010101")

        self.driver.find_element(By.ID, "contactButton").click()

        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//input[@name='fullname']/following-sibling::div"), "Field required")
        )
        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//input[@name='email']/following-sibling::div"), "Field required")
        )

        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//input[@name='phone']/following-sibling::div"), "Field required")
        )

        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//textarea[@name='message']/following-sibling::div"), "Field required")
        )


