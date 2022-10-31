import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


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

        print("Contact submitted successfully")





