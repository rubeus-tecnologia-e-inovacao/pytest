"""
Este modulo contem o POM da pagina de login do Account
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from libraries.pom import SeleniumObject

class CrudConcorrentes(SeleniumObject):

    ROUTE = "/concorrentes"
    URL = "https://crmdev6.apprbs.com.br" + ROUTE


    # Locators
    ADICIONAR_BUTTON = (By.XPATH, "//button[contains(.,'Adicionar')]")
    CONTEUDO_CRUD = (By.XPATH, "//div[@class='padding-top conteudo-crud flex-100']")


    # Interaction Methods
    def concorrentes_list(self):
        concorrentes = self.find_elements(self.CONTEUDO_CRUD)
        concorrentes_list = [concorrente.text for concorrente in concorrentes]
        return concorrentes_list