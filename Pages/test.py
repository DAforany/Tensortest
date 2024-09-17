from SBIS import SBISPage
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Tensor import Tensor
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


def findPath(browser):
    sitePath = SBISPage(browser)
    sitePath.open()
    sitePath.ClickContacts()
    browser.find_element(
        By.CLASS_NAME,
        "sbisru-Contacts__logo-tensor",
    ).click()
    print("Функция работает")
    assert browser.current_url == "https://tensor.ru/"


findPath(browser)


def chekblock(browser):
    aboutPath = Tensor(browser)
    aboutPath.open()
    aboutPath.powerIsDisplayed()
    aboutPath.ClickButton()
    assert browser.current_url == "https://tensor.ru/about"


chekblock(browser)
