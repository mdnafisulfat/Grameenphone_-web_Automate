from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.grameenphone.com/")

# click on Bangla
driver.find_element(By.XPATH, "//a[contains(text(),'বাংলা')]").click()
time.sleep(2)

if driver.current_url == "https://www.grameenphone.com/bn":
    print("Passed")
else:
    print("Fail")

# click on English
driver.find_element(By.XPATH, "//a[normalize-space()='English']").click()
time.sleep(2)

if driver.current_url == "https://www.grameenphone.com/":
    print("Passed")
else:
    print("Fail")


# click on Business
driver.find_element(By.XPATH, "//a[normalize-space()='Business']").click()
time.sleep(2)

# click on About
driver.find_element(By.XPATH, "//a[normalize-space()='About']").click()
time.sleep(2)


# click on Personal
driver.find_element(By.XPATH, "//a[normalize-space()='Personal']").click()
time.sleep(5)

# Click on search
try:

    driver.find_element(By.XPATH, "//svg[contains(@class, 'search-icon')]").click()
    time.sleep(2)


    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").send_keys("iphone")
    time.sleep(5)

except Exception:
    print(f"An error occurred")

driver.close()
print("Passed")