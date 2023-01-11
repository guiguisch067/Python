#!python3
# Python 3.9.6 64-bit
# commande permettant d'installer le package pyautogui grâce à gestionnaire pip
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyautogui --user
import pyautogui
# Commande pour arrêter le script en poussant la souris dans le coin supérieur gauche
pyautogui.FAILSAFE = True
while True:
    pyautogui.moveTo(300, 300, duration = 3)
    pyautogui.moveTo(300, 400, duration = 3)
    pyautogui.click()
    pyautogui.moveTo(400, 400, duration = 3)
    pyautogui.moveTo(400, 300, duration = 3)
