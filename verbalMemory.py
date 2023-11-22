from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://humanbenchmark.com/tests/verbal-memory")

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

# Initialize word list
wordList = []

try:
    while True:
        # Get the current word
        word = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "word"))).text

        # Click 'SEEN' if the word is in the list, otherwise click 'NEW' and add to the list
        if word in wordList:
            driver.find_element(By.XPATH, "//button[contains(text(),'SEEN')]").click()
        else:
            driver.find_element(By.XPATH, "//button[contains(text(),'NEW')]").click()
            wordList.append(word)

    time.sleep(10)

except Exception:
    driver.quit()