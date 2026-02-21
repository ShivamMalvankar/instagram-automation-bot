from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from time import sleep

INSTAGRAM_ID = "malvankarshivam70@gmail.com"
INSTAGRAM_PASS = "shivam_1234"
INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "buzzfeedtasty"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 30)
driver.get(url=INSTAGRAM_URL)


username = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="_R_32d9lplcldcpbn6b5ipamH1_"]'))
)
password = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="_R_33d9lplcldcpbn6b5ipamH1_"]'))
)
login = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div'))
)
username.click()
username.send_keys(INSTAGRAM_ID)
password.click()
password.send_keys(INSTAGRAM_PASS)
login.click()

sleep(4.3)
try:
    save_login_prompt = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
    if save_login_prompt:
        save_login_prompt.click()

except NoSuchElementException:

    continue_prompt = driver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_k4"]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div')
    if continue_prompt:
        continue_prompt.click()

sleep(5)

driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

sleep(8.2)

modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
modal = driver.find_element(by=By.XPATH, value=modal_xpath)
for i in range(5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    sleep(2)
