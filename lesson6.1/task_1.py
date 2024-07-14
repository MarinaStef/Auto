from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import *
from time import sleep

def test_data_types_form(chrome_browser):
    chrome_browser.get(URL1)
    chrome_browser.find_element(By.NAME, "first_name").send_keys(First_name)
    chrome_browser.find_element(By.NAME, "last_name").send_keys(Last_name)
    chrome_browser.find_element(By.NAME, "address").send_keys(Address)
    chrome_browser.find_element(By.NAME, "e-mail").send_keys(Email)
    chrome_browser.find_element(By.NAME, "phone").send_keys(Phone_number)
    chrome_browser.find_element(By.NAME, "zip-code").send_keys(Zip_code)
    chrome_browser.find_element(By.NAME, "city").send_keys(City)
    chrome_browser.find_element(By.NAME, "country").send_keys(Country)
    chrome_browser.find_element(By.NAME, "job_position").send_keys(Job_position)
    chrome_browser.find_element(By.NAME, "company").send_keys(Company)
    WebDriverWait(chrome_browser, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    sleep(2)
    assert "success" in chrome_browser.find_element(By.ID, "first_name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "last_name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "address").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "phone").get_attribute("class")
    assert "danger" in chrome_browser.find_element(By.ID, "zip-code").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "city").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "country").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "job_position").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "company").get_attribute("class")

    