from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# variable delcarations
updated = False


# gets username and turns into lowercase
username = input("What is your League of Legends username? \n")
username.lower()


# finds chrome driver and goes to op.gg of that username
PATH = "/Users/harshuljain/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
if not(not username):
    driver.get("https://na.op.gg/summoner/userName=" + username)
else:
    print ("Enter a username")


# updates the op.gg for the user after waiting 60 seconds
try:
    update_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "SummonerRefreshButton")))
    update_button.click()
    update_button = True
except:
    print ("update button was not clicked")


# gets the the Last Champion that you played
while (update_button):
    try:
        GameSettingInfo = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "GameSettingInfo")))
        print("The last champ " + username + " played was " + GameSettingInfo.text)
        break
    except:
        print ("The last champ that you played was not found :D")
        break
