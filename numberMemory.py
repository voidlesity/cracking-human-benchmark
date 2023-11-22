from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/number-memory")

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
        # Wait and read the number
        number = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "big-number"))).text

        # Wait for input field and submit the number
        inputField = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        inputField.send_keys(number)
        inputField.send_keys(Keys.ENTER)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'NEXT')]"))).send_keys(Keys.ENTER)

    time.sleep(10)

except Exception:
    driver.quit()