"""
Testes que cobrem o login com Account na Plataforma Rubeus
"""

import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers

from pages.cadastro_concorrente import CadastroConcorrente
from pages.crud_concorrentes import CrudConcorrentes


scenarios('../features/concorrente.feature')


# Given steps (only this steps can be fixtures)
@given("the Concorrente page is displayed", target_fixture="cadastro_concorrente_page")
def concorrente_page(logged_in_browser):
    page = CadastroConcorrente(logged_in_browser)
    page.load()
    return page


# When steps
@when(parsers.parse('user fills Name field with "{name}"'), converters={"name": str})
def fill_email(cadastro_concorrente_page, name):
    cadastro_concorrente_page.fill_name(name)

@when(parsers.parse('user fills Description field with "{description}"'), converters={"description": str})
def fill_email(cadastro_concorrente_page, description):
    cadastro_concorrente_page.fill_description(description)

@when("user clicks Salvar")
def click_salvar(cadastro_concorrente_page):
    cadastro_concorrente_page.click_salvar()


# Then steps
@then("the concorrentes crud page is displayed", target_fixture="crud_concorrentes_page")
def account_ambientes_page(browser):
    page = CrudConcorrentes(browser)
    return page

@then("crud concorrentes contains registry")
def user_has_ambientes(crud_concorrentes_page):
    assert len(crud_concorrentes_page.concorrentes_list()) > 0
