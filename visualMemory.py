from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/memory")

# Accept Cookies
time.sleep(1.5)
try:
    driver.find_element(By.XPATH, "//span[contains(text(),'AGREE')]").click()
except Exception:
    print("No cookie acceptance button found, or already accepted.")

# Start the test
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start')]"))).click()
except Exception:
    print("Start button not found")

try:
    while True:
        squares = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.active")))
        time.sleep(2.5)
        for square in squares:
            square.click()
        time.sleep(1)
        
except Exception:
    driver.quit()