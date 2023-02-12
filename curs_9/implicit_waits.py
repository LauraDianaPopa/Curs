from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# initializam chrome
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")

#sleep(3)
'''
Exemplu: Vrem sa cautam un element cu id-ul first name pe pagina
sistemul va cauta alec element, si daca il va gasi, va trece instant
la urmatoarea intructiune

Daca nu il gaseste, sistemul il va cauta pe toata durata stabilita implicita in implicit wait

'''
chrome.implicitly_wait(10)

chrome.find_element(By.ID, "first-name").send_keys("Laura")
sleep(3)
print("Instructiunea urmatoare 1")

#chrome.find_element(By.ID, "first-name_123456").send_keys("Nu gasesc")
print("Instructiune urmatoare 2")

chrome.quit()

"""
Setam implicit wait in secunde:
-o modalitate prin care definim un timp global de asteptare pana cand sa 
dea eroare cand un element nu e gasit
- se va instantia in momentul in care va fi executat instructiunea de implicit wait
si va fi distrus in momentul in care executia se incheie si browserul se inchide

Selenium va cauta toate elementele timp de x secunde (chrome.implicitly)

Diferenta dintre implicit wait si sleep este ca instructiunea de sleep va astepta orice ar
fi (va pune pauza la intrteg codul executata),

"""

