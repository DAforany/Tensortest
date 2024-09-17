from BaseApp import Base
from selenium.webdriver.common.by import By

blockPath = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[1]",
)
ButtonPath = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a",
)


class Tensor(Base):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://tensor.ru/")

    def powerIsfind(self):
        return self.find()(blockPath)

    def powerIsDisplayed(self):
        return self.powerIsfind().is_displayed()

    def findButton(self):
        return self.find()(ButtonPath)

    def ClickButton(self):
        self.findButton().click()
