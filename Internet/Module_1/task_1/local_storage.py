from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv

load_dotenv()

chrome_driver_path = os.getenv("CHROME DRIVER")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.example.com")
    driver.execute_script("localStorage.setItem('myKey', 'modsen_value');")

    value = driver.execute_script("return localStorage.getItem('myKey');")
    print(f"Value in LocalStorage: {value}")

    driver.execute_script("localStorage.removeItem('myKey');")

    value_after_delete = driver.execute_script("return localStorage.getItem('myKey');")
    print(f"Value after deleting from LocalStorage: {value_after_delete}")

finally:
    driver.quit()
