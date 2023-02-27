import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep



class Alerts(unittest.TestCase):
    RESULT_MESSAGE = (By.ID, 'result')
    ALERT_BUTTON = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT_BUTTON = (By.XPATH, '//button[text()="Click for JS Prompt"]')


    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.chrome.quit()

    #@unittest.skip
    def test_alert(self):
        self.chrome.find_element(*self.ALERT_BUTTON).click()
        sleep(3)
        obj = self.chrome.switch_to.alert           # Ne-am mutat de pe pagina noastra pe fereatsra de alerta
                                                    # si am salvat fereastra de alerta intr-o variabila obj

        # Metoda text extrage text-ul din alerta in cazul nostru (dintr-un element)
        print(f"Alert shows the following message: {obj.text}")

        obj.accept()        # metoda de accept() este echivalentul clickului pe butonul "OK" din alerta
        sleep(3)
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, "You successfully clicked an alert")

    @unittest.skip
    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        sleep(3)
        obj = self.chrome.switch_to.alert
        print(f"Confirm shows the following message: {obj.text}")

        # la fel ca si la alerta simpla, folosim metoda accept() pentru a apasa pe butonul "OK" din Confim alert
        obj.accept()
        sleep(3)
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, "You clicked: Ok")

    @unittest.skip
    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        sleep(3)
        obj = self.chrome.switch_to.alert
        print(f"Confirm shows the following message: {obj.text}")

        # metoda dismiss() ne ajuta sa simulam click-ul pe butonul de Cancel din Confirm alert
        obj.dismiss()
        sleep(3)
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, "You clicked: Cancel")

    def test_prompt(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        sleep(3)
        obj = self.chrome.switch_to.alert
        print(f"Confirm shows the following message: {obj.text}")

        text_introdus = "Iulia test"
        # introducem text in prompt folosind send_keys
        obj.send_keys(text_introdus)
        sleep(3)

        obj.accept()
        sleep(3)
        result_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(result_text, f"You entered: {text_introdus}")


