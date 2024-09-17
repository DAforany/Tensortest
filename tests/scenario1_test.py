from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Pages.scenario1_find import find1
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)


def onpage1():
    openfirstpage = find1
    h = openfirstpage.firstPage(
        find1, "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a"
    )
    return h


def onpage2():
    openpage = find1
    h = openpage.secondPage(find1, "sbisru-Contacts__logo-tensor")
    return h


def ontensorpage():
    openpage = find1
    openpage.findBlock(
        find1,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div",
    )


def chekimages():
    openpage = find1
    openpage.about(
        find1,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a",
    )
    openpage.chekImages(find1)


onpage1().click()
onpage2().click()
time.sleep(3)
if ontensorpage is False:
    print("Элемента нет")
else:
    print("Блок найден!")
chekimages()

driver.quit()
