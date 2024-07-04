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
    driver.add_cookie({"name": "myCookie", "value": "modsen_cookie"})

    cookie = driver.get_cookie("myCookie")
    print(f"Value in cookie: {cookie['value']}")

    driver.delete_cookie("myCookie")

    cookie_after_delete = driver.get_cookie("myCookie")
    print(f"Value after deleting from LocalStorage: {cookie_after_delete}")

finally:
    driver.quit()
