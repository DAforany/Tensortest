from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Pages.scenario2_find import find2
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)

def onpage1():
    openfirstpage = find2
    h = openfirstpage.openPage(
        find2, "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a"
    )
    return h
def chek(parturl):
    chekpage = find2
    chekpage.chekurl(find2, parturl)
def regionchange():
    change = find2
    change.pereezd(find2)
onpage1().click
time.sleep(2)
chek("yaroslavskaya-oblast")
if find2.findPartners(find2, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]") is False:
        print("Элемента нет")
else:
        print("Список партнёров найден!")
headY = driver.find_element(By.CLASS_NAME, "state-1")
regionchange()
chek("kamchatskij-kraj")
headK = driver.find_element(By.CLASS_NAME, "state-1")
if headY == headK:
    print("заголовок не менялся")
else:
    print("Заголовок изменился")
driver.quit()
