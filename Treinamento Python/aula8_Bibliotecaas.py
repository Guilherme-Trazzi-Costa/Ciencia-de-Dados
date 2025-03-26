import os
#import datetime
#import pyautogui


#pyautogui.press("win")
#pyautogui.write("chrome")
#pyautogui.press("enter")

#print(os.listdir("arquivos"))

#print(datetime.date.today())

lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
            if "22" in arquivo:
                  os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
                 
            else: 
                 os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")