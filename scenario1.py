from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)


def firstPage():
    driver.get("https://sbis.ru/")
    button = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a",
    )
    button.click()
firstPage()

def secondPage():
    driver.find_element(
        By.CLASS_NAME,
        "sbisru-Contacts__logo-tensor",
    ).click()
    time.sleep(3)
secondPage()

def findBlock():
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    block = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div",
    ).is_displayed()
    if block is False:
        print("Элемента нет")
    else:
        print("Блок найден!")
findBlock()

def about():
    buttonT = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a",
    )
    wait.until(EC.element_to_be_clickable(buttonT))
    time.sleep(3)
    buttonT.click()
    current_url = driver.current_url
    if current_url == "https://tensor.ru/about":
        print("URL верен")
    else:
        print("URL не верен")
about()

def chekImages():
    width0 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img",
    ).get_attribute("width")
    height0 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img",
    ).get_attribute("height")
    width1 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img",
    ).get_attribute("width")
    height1 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img",
    ).get_attribute("height")
    width2 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img",
    ).get_attribute("width")
    height2 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img",
    ).get_attribute("height")
    width3 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img",
    ).get_attribute("width")
    height3 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img",
    ).get_attribute("height")
    if (
        width0 == width1 == width2 == width3
        and height0 == height1 == height2 == height3
    ):
        print("Изображения равны")
    else:
        print("Изображения разного размера")
chekImages()
driver.quit()
