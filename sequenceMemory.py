from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/sequence")

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

def getSequence():
    squares = []
    while True:
        try:
            squares.append(WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.active"))))
            time.sleep(0.5)
        except:
            break
    return squares

try:
    while True:
        sequence = getSequence()
        for square in sequence:
            square.click()

except Exception:
    driver.quit()