from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)

class find2():
    def openPage(self, xpath):
        driver.maximize_window()
        driver.get("https://sbis.ru/")
        button = driver.find_element(
            By.XPATH,
            xpath,
        )
        return button

    def chekurl(self, parturl):
        if parturl in driver.current_url:
            print("Регион определён верно")
        else:
            print("Ошибка, регион определён не верно")
    def findPartners(self, xpath):
        exist = driver.find_element(
            By.XPATH,
            xpath,
        ).is_displayed()
    def pereezd(self):
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