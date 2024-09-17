from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)

class find1:
    def firstPage(self, xpath):
        driver.get("https://sbis.ru/")
        button = driver.find_element(
            By.XPATH,
            xpath,
        )
        return button

    def secondPage(self, CLASS_NAME):
        button = driver.find_element(
            By.CLASS_NAME,
            CLASS_NAME,
        )
        return button

    def findBlock(self, xpath):
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        block = driver.find_element(
            By.XPATH,
            xpath,
        ).is_displayed()
        return block

    def about(self, xpath):
        buttonT = driver.find_element(
            By.XPATH,
            xpath,
        )
        wait.until(EC.element_to_be_clickable(buttonT))
        buttonT.click()

    def chekImages(self):
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
    driver.quit()
