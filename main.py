#Automating a Youtube video
#Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DRIVER_PATH ="C:\development\chromedriver.exe"
DRIVER_SERVICE = Service(executable_path=DRIVER_PATH)

URL ="https://www.youtube.com/"
SEARCH="Let Her Go"

#Creating a class
class Bot:
    def __init__(self,driver_service,driver_path):
        self.driver_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=driver_service)

    def search_bar(self):
        time.sleep(2)
        self.driver.get(URL)
        search_bar = self.driver.find_element(By.NAME, 'search_query')
        time.sleep(2)
        search_bar.send_keys(SEARCH)
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

    def song(self):
        song = self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        time.sleep(1)
        song.click()

#Creating the objects and calling the functions
bot = Bot(DRIVER_SERVICE,DRIVER_PATH)
bot.search_bar()
bot.song()

#End of Program