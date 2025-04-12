import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load credentials from .env
load_dotenv()

USERNAME = 'admin'
PASSWORD = os.getenv('ADMIN_PASSWORD')

LOGIN_URL = "http://127.0.0.1:1337/"
MESSAGES_URL = "http://127.0.0.1:1337/messages/"

# Setup headless Chromium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1200x800")
options.binary_location = "/usr/bin/chromium"

# Use system-installed Chromedriver path
service = Service("/usr/bin/chromedriver")

# Launch driver
driver = webdriver.Chrome(service=service, options=options)

def log(msg):
    print(f"[+] {msg}")

try:
    log("Launching admin bot...")
    driver.get(LOGIN_URL)

    log("Waiting for login page to load...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email_or_username"))
    )

    log("Filling in login form...")
    driver.find_element(By.ID, "email_or_username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/user"))
    log("Login successful.")

    while True:
        log("Visiting /messages...")
        driver.get(MESSAGES_URL)
        time.sleep(3)  # Allow time for any injected JS to run

        messages = driver.find_elements(By.CLASS_NAME, "message")
        if messages:
            last_message = messages[-1].text
            log(f"Last message: {last_message}")
        else:
            log("No messages found.")

        time.sleep(5)

except Exception as e:
    log(f"[!] Error: {e}")
    with open("admin_error_dump.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    log("[!] Page source dumped to admin_error_dump.html")

finally:
    driver.quit()
