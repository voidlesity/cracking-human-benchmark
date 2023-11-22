from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the typing test page
driver.get("https://humanbenchmark.com/tests/typing")

# Accept Cookies
time.sleep(1.5)
try:
    driver.find_element(By.XPATH, "//span[contains(text(),'AGREE')]").click()
except Exception:
    print("No cookie acceptance button found, or already accepted.")

try:
    letters = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.incomplete")))
    text = ''.join([letter.get_attribute("textContent") for letter in letters])

    # Find the input field
    inputElement = driver.find_element(By.CLASS_NAME, "letters")
    
    # Send the entire text at once
    inputElement.send_keys(text)

    time.sleep(10)

except Exception:
    driver.quit()
