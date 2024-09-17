from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)


def openPage():
    driver.maximize_window()
    driver.get("https://sbis.ru/")
    button = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a",
    )
    button.click()


openPage()
time.sleep(2)


def chekurl(parturl):
    if parturl in driver.current_url:
        print("Регион определён верно")
    else:
        print("Ошибка, регион определён не верно")


chekurl("yaroslavskaya-oblast")


def findPartners():
    exist = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]",
    ).is_displayed()
    if exist is False:
        print("Элемента нет")
    else:
        print("Список партнёров найден!")


findPartners()
headY = driver.find_element(By.CLASS_NAME, "state-1")


def pereezd():
    buttonT = driver.find_element(
        By.CLASS_NAME,
        "sbis_ru-Region-Chooser__text",
    )
    buttonT.click()
    time.sleep(5)
    buttonR = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span",
    )
    wait.until(EC.element_to_be_clickable(buttonR))
    buttonR.click()
    time.sleep(1)


pereezd()
chekurl("kamchatskij-kraj")
headK = driver.find_element(By.CLASS_NAME, "state-1")
if headY == headK:
    print("заголовок не менялся")
else:
    print("Заголовок изменился")
driver.quit()
