from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://formation.bienvenue.pro/signature/0E55-44C5")

time.sleep(5)

try:
    name_sign = driver.find_element(By.XPATH, "//*[text()='VOMIANDRY Jolhan']")
    name_sign.click()
except Exception as e:
    print("Le bouton 'VOMIANDRY Jolhan' n'est pas trouvé :", e)

time.sleep(5)

help_sign = driver.find_element(By.XPATH,"/html/body/main/div/form/div[2]/div[2]/div")
help_sign.click()

time.sleep(5)

canvas = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[2]/div/div/canvas")
canvas.click()

time.sleep(1)

# Action pour dessiner "JV" sur le canvas
actions = ActionChains(driver)

actions.move_to_element_with_offset(canvas, 0, 0) # Point d'origine de l'écriture, se place sur le canvas
actions.click_and_hold()

# move_by_offset effectuer une ligne d'une longeur x,y en partant du dernier arret 
actions.move_by_offset(0, -50)

actions.move_by_offset(50, 0)

actions.move_by_offset(0, 100)

actions.move_by_offset(-25, 25)

actions.move_by_offset(-25, -25)

actions.move_by_offset(50, -50)

actions.move_by_offset(50, 50)

actions.move_by_offset(50, -50)

actions.move_by_offset(50, -50)

actions.release() # Leve le curseur
actions.perform() # effectue les actoins stocker

time.sleep(10)

help_sign = driver.find_element(By.XPATH,"/html/body/main/div/form/div[3]/div/div[3]/div/button")
help_sign.click()

driver.quit()
