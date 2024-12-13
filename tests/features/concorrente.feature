@concorrentes @web
Feature: Login Rubeus Account
    As a registered user
    User wants to manage the competitors list

    Background:
        Given I am logged in as a valid user

    @concorrentes
    Scenario Outline: Register a concorrente
        Given the Concorrente page is displayed
        When user fills Name field with "<name>"
        And user fills Description field with "<description>"
        And user clicks Salvar
        Then the concorrentes crud page is displayed
        And crud concorrentes contains registry

        Examples: Wrong_user
            |       name        |    description         |
            | Uniexemplo        | Primeiro concorrente   |
            | Uniconcorre       | Segundo concorrente    |