from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def test_valid_login():
    driver = webdriver.Chrome()

    file_path = "file://" + os.path.abspath("login.html")
    driver.get(file_path)

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

    message = driver.find_element(By.ID, "message").text
    assert message == "Login Successful"

    driver.quit()
