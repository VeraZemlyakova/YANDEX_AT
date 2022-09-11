import pytest
from os import getcwd
from termcolor import colored
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(executable_path=getcwd() + '\\driver\\geckodriver.exe')
    yield driver
    driver.quit()


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases. """

    item._nodeid = colored(item._obj.__doc__, 'magenta')
