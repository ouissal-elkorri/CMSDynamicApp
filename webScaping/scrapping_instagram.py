#http://www.easy2digital.com/automation/data/python-tutorial-for-digital-marketer-12-using-hashtags-to-scrape-top-instagram-posts-and-instagram-users/
#$pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time

query = "art"
link = []
def get_instagram_hashtags_list(query):
    driver = webdriver.Chrome('C:/Users/user/Desktop/S6/internship/cnrst/chromedriver')
    driver.get("http://www.instagram.com")

    #target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    #enter username and password
    username.clear()
    username.send_keys("random_shitty_digital_art")
    password.clear()
    password.send_keys("Hunuuuuu1998@")

    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #We are logged in!

    #posts that are related to a specific hashtag :)

    page = driver.get("https://www.instagram.com/explore/tags/" + query)
    driver.execute_script("window.scrollBy(0,1000000)")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,1000000)")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,1000000)")
    time.sleep(5)
    Ma_Liste = []

    i = 0
    source = driver.find_elements_by_tag_name('img')

    for src in source:
        links = driver.find_elements_by_tag_name('a')

        info = {
            "link_ig": links[i].get_attribute('href'),
            "src_img": src.get_attribute('src')
        }
        Ma_Liste.append(info)
        i += 1

    return (Ma_Liste)

"""
link = get_instagram_hashtags_list(query)
print(link)
"""
