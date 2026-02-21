from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from dotenv import load_dotenv
import os
from time import sleep

# Load environment variables
load_dotenv()

INSTAGRAM_ID = os.getenv("INSTAGRAM_ID")
INSTAGRAM_PASS = os.getenv("INSTAGRAM_PASS")

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "buzzfeedtasty"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 30)
driver.get(url=INSTAGRAM_URL)

# Username field
username = wait.until(
    EC.element_to_be_clickable((By.NAME, "username"))
)

# Password field
password = wait.until(
    EC.element_to_be_clickable((By.NAME, "password"))
)

# Login button
login = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)

username.send_keys(INSTAGRAM_ID)
password.send_keys(INSTAGRAM_PASS)
login.click()

sleep(5)

# Handle popups safely
try:
    not_now = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
    )
    not_now.click()
except:
    pass

sleep(3)

# Go to followers page
driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

sleep(5)

# Scroll followers modal
modal = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul/.."))
)

for _ in range(5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    sleep(2)