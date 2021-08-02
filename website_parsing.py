from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
import time


driver = webdriver.Chrome("C:\\Users\\nidhi\\Documents\\ntu-automate-star-wars-master\\chromedriver.exe")
driver.get("https://ap.louisvuitton.com/")

#target the new button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='lv-header-main-nav__item']"))).click()
time.sleep(5)

button2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='nvcat1830005v-button']"))).click()

button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/eng-sg/new/for-women/the-latest/_/N-130yg6f']"))).click()

#button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='lv-smart-link lv-product-card__url']"))).click()
