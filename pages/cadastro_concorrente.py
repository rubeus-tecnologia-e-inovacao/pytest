"""
Este modulo contem o POM da pagina de login do Account
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from libraries.pom import SeleniumObject

class CadastroConcorrente(SeleniumObject):

    # ROUTE = "/cadastro-concorrente"
    URL = "https://crmdev6.apprbs.com.br/cadastro-concorrente" 


    # Locators
    NAME_INPUT = (By.XPATH, "//input[@formcontrolname='name']")
    DESCRIPTION_INPUT = (By.XPATH, "//input[@formcontrolname='description']")
    SAVE_BUTTON = (By.XPATH, "//span[@class='mdc-button__label'][contains(.,'Salvar')]")

    # Interaction Methods
    def fill_name(self, name):
        name_input = self.find_element(self.NAME_INPUT)
        name_input.send_keys(name)

    def fill_description(self, description):
        description_input = self.find_element(self.DESCRIPTION_INPUT)
        description_input.send_keys(description)

    def click_salvar(self, timeout=10):
        salvar = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((self.SAVE_BUTTON))
        )
        salvar.click()
