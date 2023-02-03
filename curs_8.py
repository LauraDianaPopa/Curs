from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Selectors():
    chrome = webdriver.Chrome(ChromeDriverManager().install())

# cream constante in functie de selectorii pe care o sa-i folosim
    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LAST_NAME = (By.CLASS_NAME, "form-control")
    RADIO_BUTTON_1 = (By.CSS_SELECTOR, "input#radio-button-1")
    RADIO_BUTTON_2 = (By.CSS_SELECTOR, "input#radio-button-2")
    RADIO_BUTTON_3 = (By.CSS_SELECTOR, "input#radio-button-3")
    AUTOCOMPLETE_LINK_TEXT = (By.LINK_TEXT, "Autocomplete")
    ENABLED_DISABLED_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Enabled")
    INPUT_FIRST_NAME_BY_XPATH = (By.XPATH, "//input[@id='first-name']")

    def __init__(self):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        self.chrome.maximize_window()

    def first_name_field(self, first_name):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        first_name_text_field = self.chrome.find_element(*self.INPUT_FIRST_NAME)# first_name_text_field va fi elementul de pe pagina cu Id-ul first-name
        first_name_text_field.send_keys(first_name)

    def last_name_field(self, last_name):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        last_name_text_field = self.chrome.find_elements(*self.INPUT_LAST_NAME)# pentru a returna toate elementele cu aceslasi classname/id/tag/name trebuie apelat find_elements
        last_name_text_field[1].send_keys(last_name)

    def click_radio_button(self, number=0):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        if number == 1:
            self.chrome.find_element(*self.RADIO_BUTTON_1).click()
        elif number==2:
            self.chrome.find_element(*self.RADIO_BUTTON_2).click()
        elif number == 3:
            self.chrome.find_element(*self.RADIO_BUTTON_3).click()
        else:
            self.chrome.find_element(*self.RADIO_BUTTON_1).click()
            self.chrome.find_element(*self.RADIO_BUTTON_2).click()
            self.chrome.find_element(*self.RADIO_BUTTON_3).click()

    def click_autocomplete(self):
        self.chrome.get("https://formy-project.herokuapp.com")
        self.chrome.find_element(*self.AUTOCOMPLETE_LINK_TEXT).click()

    def click_enabled(self):
        self.chrome.get("https://formy-project.herokuapp.com")
        self.chrome.find_element(*self.ENABLED_DISABLED_LINK_TEXT).click()

    def input_first_name_by_xpath(self, firstname):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        self.chrome.find_element(*self.INPUT_FIRST_NAME_BY_XPATH).send_keys(firstname)

    def formy_input(self, placeholder_text, input_value):
        #self.chrome.get("https://formy-project.herokuapp.com/form")
        input = self.chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
        input.clear()
        input.send_keys(input_value)








selector = Selectors()
# selector.first_name_field("Laura")
# #sleep(5)
# selector.last_name_field('Popa')
# selector.click_radio_button(3)
# selector.click_autocomplete()
# #sleep(2)
# selector.click_enabled()
#selector.first_name_field("Laura")
selector.input_first_name_by_xpath("Laura")
sleep(2)
selector.formy_input("Enter first name", "Diana")
selector.formy_input("Enter last name", "Popa")
selector.formy_input("Enter your job title", "QA Automation Engineer")
sleep(5)



