from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Enable headless mode
options = Options()
options.headless = True

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/reactiontime")

# Accept Cookies
time.sleep(1.5)
try:
    driver.find_element(By.XPATH, "//span[contains(text(),'AGREE')]").click()
except Exception:
    print("No cookie acceptance button found, or already accepted.")

try:
    WebDriverWait(driver, 5, 0.1).until(EC.element_to_be_clickable((By.CLASS_NAME, "view-splash"))).click()

    while True:
        # Wait for green screen and click
        WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located((By.CLASS_NAME, "view-go"))).click()

        # Click to continue
        WebDriverWait(driver, 5, 0.01).until(EC.presence_of_element_located((By.CLASS_NAME, "view-result"))).click()

    time.sleep(10)

except Exception:
    driver.quit()