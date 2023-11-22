from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/chimp")

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
        # Wait until the numbers appear
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-cellnumber]")))

        # Find all elements with numbers
        numberElements = driver.find_elements(By.CSS_SELECTOR, "[data-cellnumber]")
        
        # Extract numbers and corresponding elements
        numbers = [(int(elem.get_attribute("data-cellnumber")), elem) for elem in numberElements]

        # Sort the numbers in ascending order
        numbers.sort(key=lambda x: x[0])

        # Click the elements in the sorted order
        for _, number in numbers:
            number.click()
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).send_keys(Keys.ENTER)

    time.sleep(10)

except Exception:
    driver.quit()