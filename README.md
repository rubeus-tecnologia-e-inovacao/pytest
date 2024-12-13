# Overview 📚

- [Installation](#installation)
- [Folder structure](#folder-structure)
- [How to contribute](#how-to-contribute)



## Installation

1. **Requirements:**
   - Python: `v3.10` or recent
   - Pip: Package Installer for Python. [Documentation](https://pypi.org/project/pip/)
   - Pipenv: Python virtualenv management tool. [Documentation](https://pipenv.pypa.io/en/latest/)

2. **Clone and run:**
   - Clone the repository to your local development environment.

   ```bash
   git clone git@github.com:rubeus-tecnologia-e-inovacao/pytest.git
   cd pytest
   pipenv install
   pipenv run python -m pytest
    ```
   - Run with multithread.

   ```bash
   pipenv run python -m pytest -n 4
    ```
   ```bash
    - Run with docker (Just GRID in containers now)

    If using Windows: Install WSL

- Install docker
- pull selenium hub image
- pull selenium node <'browser'> image

Start WSL
Open docker desktop

- run: docker-compose up -d
- run: docker ps -a

    ```


### config.json template

 We recommend using an admin user

```
{
    "browser": "Chrome",
    "type": "local",
    "implicit_wait": 10,
    "url_remote": "http://localhost:4444/wd/hub",
    "environment": "https://crmenvironment.apprubeus.com.br",
    "valid_user": "usuario@rubeus.com.br",
    "valid_password": "123exemplo"
}
```  

## Folder Structure

The `components/common` folder contains all the components used throughout the application, each feature will have its own `/components` folder if that component is very specific and will not be used again.

### Component specific folder

- Structure

- **/components**
  - _Global components here..._

- **/pages**
  - **/auth**
    - **/components**

  - **/dashboard**
    - **/components**

Just follow this pattern for specific components, otherwise throw everything in the `/components/common` folder


## How to Contribute

### 1. First open an issue

Before submitting any changes, open an issue describing the reason for the change and the proposed solution. If the issue is approved, you may proceed to the next step below.

### 2. Open a Pull Request

After the issue is approved and you've made the necessary changes, open a pull request. The code will then be evaluated by me, and if everything is satisfactory, I will accept the change.