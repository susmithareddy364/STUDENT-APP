from selenium import webdriver
from selenium.webdriver.common.by import By


def test_enter_student_name():

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000")

    name_field = driver.find_element(By.ID, "name")

    name_field.send_keys("John Smith")

    assert name_field.get_attribute("value") == "John Smith"

    driver.quit()