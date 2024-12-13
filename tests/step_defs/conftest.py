"""
This module contains shared fixtures
"""

import json
import pytest
from pytest_bdd import given
import pytest_html  
import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
from datetime import datetime


servico = Service(ChromeDriverManager().install())

# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# This fixture run only one time before the entire test suite
@pytest.fixture
def config(scope='session'):
    
    # Read config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert config['type'] in ['local', 'remote']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    assert isinstance(config['url_remote'], str)
    assert len(config['url_remote']) > 0
    assert isinstance(config['crm_environment'], str)
    assert len(config['crm_environment']) > 0

    # Return a dictionary of configs
    return config


# This fixture will run once for each test case
@pytest.fixture
def browser(config):

    #Inicializa uma instancia do WebDriver
    if config['type'] == 'local':

        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
            opts.add_argument('--window-size=1366,768')
            b = webdriver.Firefox(options=opts)
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('--window-size=1366,768')
            b = webdriver.Chrome(service=servico, options=opts)
        elif config['browser'] == 'Headless Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('headless')
            b = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    elif config['type'] == 'remote':
        
        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()

        opts.add_argument('--no-sandbox')

        b = webdriver.Remote(
            command_executor = config['url_remote'],
            options=opts
        )

    else:
        raise Exception(f'Type "{config["type"]}" is not supported')

    #Faz o navegador esperar até 10s pro elemento aparecer
    b.implicitly_wait(config['implicit_wait'])

    #Retorna a instancia do webdriver para configuracao
    yield b

    #Sai da instancia do WebDriver (limpa ao fim do teste)
    b.quit()


@pytest.fixture
def login_credentials(config):
    return {
        'email': config['valid_user'],
        'password': config['valid_password']
    }


# Browser authentication
@pytest.fixture
def login(browser, config):
    timeout = 10
    browser.get(config["account_environment"])  # URL da página de login do account
    browser.find_element(By.XPATH, "(//input[@class='mdc-text-field__input'])[1]").send_keys(config["valid_user"])
    browser.find_element(By.XPATH, "(//input[@class='mdc-text-field__input'])[2]").send_keys(config["valid_password"])
    entrar = WebDriverWait(browser, timeout).until( 
        EC.element_to_be_clickable((By.XPATH, "//div[@class='mdc-form-field mdc-form__item'][contains(.,'Entrar')]")) )
    entrar.click()
    time.sleep(0.5)
    return browser


# Shared given steps
@given("I am logged in as a valid user", target_fixture="logged_in_browser")
def logged_in_user(login):
    return login  # Garante que o estado do usuário autenticado seja reutilizado
