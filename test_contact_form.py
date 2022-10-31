import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://unicreds.com/contact-us")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID, "fullname").send_keys("Test Automation")
        driver.find_element(By.NAME, "email").send_keys("test@yopmail.com")
        driver.find_element(By.ID, "phone").send_keys("0101010101")
        driver.find_element(By.ID, "phone").send_keys("Testing")
        time.sleep(2)


run = DragDrop()
run.drag_drop()
