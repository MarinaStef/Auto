from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(5)

try:
    driver.get("http://uitestingplayground.com/ajax")
    blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_from_content = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".bg-success"))).text
    print(text_from_content)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
