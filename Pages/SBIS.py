from BaseApp import Base
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

ButtonPath = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a",
)

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser

class SBISPage(Base):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://sbis.ru/")
        driver = webdriver.Chrome()
        driver.get("https://sbis.ru/")
        wait = WebDriverWait(driver, timeout=2)

    def findContacts(self):
        return self.find(ButtonPath)

    def ClickContacts(self):
        self.findContacts().click()
