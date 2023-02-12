import unittest

from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Test(TestCase):
   #Elemete de pe pagina pe care o testam
   #in loc sa le repetam pentru fiecare test, il scriu aici si il folosesc de
   #cate ori am nevoie
    FORM_LINK = (By.LINK_TEXT, "Form")
    INPUT_FIRST_NAME=(By.ID, "first-name")

    # Se ruleaza inainte de fiecare test-> face setup pentru teste
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://formy-project.herokuapp.com/")
        #unpack la tupla ,-.(By.LINK_TEXT,"Form")-> By LINK_TEXT, "Form"
        self.chrome.find_element(*self.FORM_LINK).click()
        #daca nu facem unpack ar arata asa self. chrome.find_element(By.LINK_TEXT,"Form")-> By LINK_TEXT, "Form"
        #daca facem unpack ........
        #se ru;eaza dupa fiecare test si are rolul de cleanup dupa fiecare test

    def tearDown(self):
        self.chrome.quit()

        #numele metodei trebuie sa inceapa cu test, altfel unittest nu va sti sa recunoasca metoda
    def test_url(self):
        expected_url = "https://formy-project.herokuapp.com/form"
        actual_url = self.chrome.current_url
        assert actual_url == expected_url, f'URL incorect :{actual_url}'

    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "Formy"
        assert actual_title == expected_title," Titlul paginii nu este corect"

#facem skip la acest test
    @unittest.skip
    def test_first_name(self):
        first_name = self.chrome.find_element(*self.INPUT_FIRST_NAME)
        #!!!! first_name.text nu returneaza nimic
        first_name.send_keys("Laura")
        expected = "Laura"
        actual = first_name.text
        assert actual == expected, f"Textul introdus nu este cel asteptat actual={actual}"




    def test_element_displayed(self):
        first = self.chrome.find_element(*self.INPUT_FIRST_NAME)
        self.assertTrue(first.is_displayed(), "Elementul nu a fost gasit")
#metode incorecta de verificare a inexistentei unui element
    def test_element_not_displayed(self):
        element_inexistent= self.chrome.find_element(By.ID, "Element inexistent")
        self.assertFalse(element_inexistent.is_displayed()," Elementul exista desi nu il gasim")

   #varianta corecta de verificare a inexistentei unui element
   #folosim try-except si prindem exceptia NoSuchElementException
    def test_element_not_displayed(self):
        try:
            self.chrome.find_element(By.ID,"Element inexistent")
        except NoSuchElementException:
            pass
#varianta corecta de verificare a inexistentei a unui element
   #facem cu find elements, care returneaza o lista
   #verificam daca lista este goala, deoarece find_elements nu arunca eroare daca nu gaseste nici un element
   
    def test_element_not_displayed_2(self):
        elements = self.chrome.find_elements(By.ID, "Element inexistent")
        self.assertTrue(len(elements) == 0, "Cel putin un element a fost gasit")