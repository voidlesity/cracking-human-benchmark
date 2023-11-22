from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Enable headless mode
options = Options()
options.headless = True

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/aim")

# Accept Cookies
time.sleep(1.5)
try:
    driver.find_element(By.XPATH, "//span[contains(text(),'AGREE')]").click()
except Exception:
    print("No cookie acceptance button found, or already accepted.")

try:
    while True:
        target = WebDriverWait(driver, 0.5, 0.01).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-1k4dpwl > div:nth-child(1)')))
        ActionChains(driver).move_to_element(target).click().perform()

except Exception:
    time.sleep(10)
    driver.quit()