from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pyautogui
pyautogui.PAUSE = 10
time_action = 15

# ENTRADA DE DADOS
login = 'mais.1pagina'
senha = '362282shkp'

picture_post = 'teste2.png'
file_comentario = f'comentarios_{login}'
marca_pessoas = 'marcar'


browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
sleep(time_action)

# sistema de login
login_digita = '//*[@id="loginForm"]/div/div[1]/div/label/input'
browser.find_element(By.XPATH, login_digita).send_keys(login)
sleep(time_action)
senha_digita = '//*[@id="loginForm"]/div/div[2]/div/label/input'
browser.find_element(By.XPATH, senha_digita).send_keys(senha)
sleep(time_action)
enter = '//*[@id="loginForm"]/div/div[3]/button/div'
browser.find_element(By.XPATH, enter).click()
sleep(time_action)

# sistema agora não
agora_nao_1 = '//*[@id="react-root"]/section/main/div/div/div/div/button'
browser.find_element(By.XPATH, agora_nao_1).click()
sleep(time_action)
agora_nao_2 = '/html/body/div[6]/div/div/div/div[3]/button[2]' or '/html/body/div[5]/div/div/div/div[3]/button[2]'
browser.find_element(By.XPATH, agora_nao_2).click()
sleep(time_action)

# sistema postar
botao_postar = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div'
browser.find_element(By.XPATH, botao_postar).click()
sleep(time_action)
escolher_arquivo = '/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'
browser.find_element(By.XPATH, escolher_arquivo).click()
sleep(time_action)

# sistema seleçao de post
sleep(time_action)
pyautogui.press('left', 4)
pyautogui.press('right')
pyautogui.hotkey('enter')
pyautogui.press('right', 2)
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('bots_posts', 1)
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite(login, 1)
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite(f'posts_{login}', 1)
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite(picture_post, 1)
pyautogui.hotkey('enter')

# click avança -> avança
avanca1 = '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'
avanca2 = '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'
browser.find_element(By.XPATH, avanca1).click()
sleep(time_action)
browser.find_element(By.XPATH, avanca2).click()
sleep(time_action)

# marcar pessoas
# area_de_marcar = '/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
# navegador.find_element(By.XPATH, area_de_marcar).click()
# pyautogui.typewrite(marca_pessoas, 0.5)

# comentarios
sleep(time_action)
pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.typewrite(f'cd bots_posts/{login}', 1)
pyautogui.hotkey('enter')
pyautogui.typewrite(f'gedit {file_comentario}', 1)
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'f4')
pyautogui.typewrite('exit')
pyautogui.hotkey('enter')

comenter_click = '/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea'
browser.find_element(By.XPATH, comenter_click).click()
pyautogui.hotkey('ctrl', 'v')

# click compartilhar
compartilha = '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'
browser.find_element(By.XPATH, compartilha).click()
sleep(time_action)

pyautogui.hotkey('f5')
sleep(time_action)

# sair da conta
icone_perfil = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span'
browser.find_element(By.XPATH, icone_perfil).click()
sleep(time_action)
sair = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div'
browser.find_element(By.XPATH, sair).click()
sleep(time_action)

# remove file (gambiara)
sleep(time_action)
pyautogui.hotkey('ctrl', 'alt', 't')
sleep(time_action)
pyautogui.typewrite(f'cd /home/guilhermembfi/bots_posts/{login}/posts_{login}', 1)
pyautogui.hotkey('enter')
pyautogui.typewrite('rm', 1.5)
pyautogui.press('space')
pyautogui.typewrite(picture_post, 1)
pyautogui.press('enter')
pyautogui.typewrite('exit', 1)
pyautogui.hotkey('enter')
