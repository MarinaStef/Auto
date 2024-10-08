from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
waiter = WebDriverWait(driver, 20)
driver.get(
    "http://uitestingplayground.com/ajax")
driver.find_element(By.ID, "ajaxButton").click()
waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success')))
print(driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text)