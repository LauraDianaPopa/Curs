from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

"""
CHROME --------------------------------------------------------------------------
# pentru a rula teste pe Chrome, cu versiunea selenium 4.6.0
driver = webdriver.Chrome()

# pentru a rula teste pe Chrome cu o versiune dinainte de selenium 4.6.0
s = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


FIREFOX --------------------------------------------------------------------------
# pentru a rula teste pe Firefox, cu versiunea selenium 4.6.0
driver = webdriver.Firefox()

# pentru a rula teste pe Firefox cu o versiune dinainte de selenium 4.6.0
s = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=s)

EDGE--------------------------------------------------------------------
# pentru a rula teste pe Edge, cu versiunea selenium 4.6.0
driver = webdriver.Edge()

# pentru a rula teste pe Edge cu o versiune dinainte de selenium 4.6.0 
s = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=s)
"""

driver = webdriver.Edge()

driver.maximize_window()

driver.get('https://formy-project.herokuapp.com/form')

first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('iulia')

sleep(3)

driver.quit()