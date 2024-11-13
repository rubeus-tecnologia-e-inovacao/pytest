"""
Este modulo contem o POM da pagina de Ambientes do Account
"""

from selenium.webdriver.common.by import By
from libraries.pom import SeleniumObject

class AccountAmbientesPage(SeleniumObject):

    URL = "https://login.rubeus.com.br/ambientes"

# Locators
    AMBIENTES = (By.XPATH, "(//div[@class='listItem'])")
    SEARCH_INPUT = (By.XPATH, "//input[@class='search-class-input']")
    TITLE_H1 = (By.XPATH, "//h1[@class='my-environments']")


    def meus_ambientes(self):
        ambientes = self.find_elements(self.AMBIENTES)
        meus_ambientes = [ambiente.text for ambiente in ambientes]
        return meus_ambientes

    def search_input_value(self):
        search_input = self.find_element(self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        title_h1 = self.find_element(self.TITLE_H1)
        return title_h1
