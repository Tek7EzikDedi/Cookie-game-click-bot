from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

click = driver.find_element(By.XPATH, '//*[@id="cookie"]')
finish_time = time.time() + 60*5
while True:
    end_time = time.time() + 10
    while True:
        click.click()
        if time.time() > end_time:

            money = int(driver.find_element(By.XPATH, '//*[@id="money"]').text.replace(",", ""))
            cursor_money = int(driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.replace("Cursor - ", "").replace(",", ""))
            grandma_money = int(driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.replace("Grandma - ", "").replace(",", ""))
            factory_money = int(driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.replace("Factory - ", "").replace(",", ""))
            mine_money = int(
                driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.replace("Mine - ", "").replace(",", ""))
            shipment_money = int(
                driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text.replace("Shipment - ", "").replace(",",
                                                                                                                  ""))
            alchemy_lab_money = int(
                driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.replace("Alchemy lab -", "").replace(
                    ",", ""))
            portal_money = int(
                driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').text.replace("Portal - ", "").replace(",", ""))
            time_machine_money = int(
                driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.replace("Time machine - ",
                                                                                           "").replace(",", ""))
            if money >= time_machine_money:
                driver.find_element(By.XPATH, '//*[@id="buyTime machine"]').click()
            elif money >= portal_money:
                driver.find_element(By.XPATH, '//*[@id="buyPortal"]').click()
            elif money >= alchemy_lab_money:
                driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]').click()
            elif money >= shipment_money:
                driver.find_element(By.XPATH, '//*[@id="buyShipment"]').click()
            elif money >= mine_money:
                mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]').click()
            elif money >= factory_money:
                factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]').click()
            elif money >= grandma_money:
                driver.find_element(By.XPATH, '//*[@id="buyGrandma"]').click()
            else:
                driver.find_element(By.XPATH, '//*[@id="buyCursor"]').click()

            if time.time() > finish_time:
                print(driver.find_element(By.XPATH, '//*[@id="cps"]').text)
            break



