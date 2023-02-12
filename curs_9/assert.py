from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# initializam chrome
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/")

chrome.find_element(By.LINK_TEXT,"Autocomplete").click()

expected_url = "https://formy-project.herokuapp.com/autocomplete"

actual = chrome.current_url

assert actual == expected_url, f"Invalid url: expected->{expected_url},actual->{actual}"

chrome.quit()