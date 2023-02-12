from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# initializam chrome
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")
chrome.implicitly_wait(5)

#explicit wait, asteapta 15 sec pt elementul cu idfirst-name
first_name = WebDriverWait(chrome,15).until(EC.presence_of_element_located((By.ID,'first-name')))
first_name.send_keys("Laura")

#se asteapta implicit 5 secunde deoarece am specificat acest lucru la linia 14
last_name = chrome.find_element(By.ID, "last-name")
last_name.send_keys("Popa")

#sleep(3)