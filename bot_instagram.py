from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os
import pyautogui

pyautogui.PAUSE = 10
time_05seg = 5
time_10seg = 10
time_20seg = 20

# ENTRADA DE DADOS

login = 'mais.1pagina'
password = '362282shkp'
file_post = f'/home/guilhermembfi/bots_posts/{login}/pictures/'
file_comment = f'/home/guilhermembfi/bots_posts/{login}/comments/'
number_posts = int(input('Quantos posts quer fazer: '))


if number_posts == 0:
    number_posts = 1
else:
    number_posts = number_posts

dir_pictures = sorted(os.listdir(file_post))
dir_comment = sorted(os.listdir(file_comment))

item_1_picture = dir_pictures[0]
item_1_comment = dir_comment[0]

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
sleep(time_10seg)


def system_login(login_def, password_def):
    time_05seg_def = 5
    write_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    browser.find_element(By.XPATH, write_login).send_keys(login_def)
    sleep(time_05seg_def)
    write_password = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    browser.find_element(By.XPATH, write_password).send_keys(password_def)
    sleep(time_05seg_def)
    button_enter = '//*[@id="loginForm"]/div/div[3]/button/div'
    browser.find_element(By.XPATH, button_enter).click()
    sleep(time_05seg_def)
    
    
def system_now_no():
    time_10seg_def = 10
    now_no_1 = '#react-root > section > main > div > div > div > div > button'
    browser.find_element(By.CSS_SELECTOR, now_no_1).click()
    sleep(time_10seg_def)
    now_no_2 = 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm'
    browser.find_element(By.CSS_SELECTOR, now_no_2).click()
    sleep(time_10seg_def)
    

def system_click_to_post():
    time_10seg_def = 10
    click_button_post = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div'
    browser.find_element(By.XPATH, click_button_post).click()
    sleep(time_10seg_def)
    click_choice_file = 'body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.uY' \
                        'zeu > div._C8iK > div > div > div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.kEKum > div > button'
    browser.find_element(By.CSS_SELECTOR, click_choice_file).click()
    sleep(time_10seg_def)


def to_directory_bot_posts():
    pyautogui.PAUSE = 5
    pyautogui.press('left', 4)
    pyautogui.press('right')
    pyautogui.hotkey('enter')
    pyautogui.press('right', 2)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('bots_posts', 1)
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')


def to_directory_login_name(login_def):
    pyautogui.PAUSE = 5
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite(login_def, 1)
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')


def get_file_picture(item_1_picture_def):
    pyautogui.PAUSE = 5
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('pictures', 1)
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite(item_1_picture_def, 1)
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')


def system_choice_post(login_def, item_1_picture_def):
    to_directory_bot_posts()
    to_directory_login_name(login_def)
    get_file_picture(item_1_picture_def)


def system_advance():
    time_10seg_def = 10
    button_advance_1 = 'body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.' \
                       'eGOV_.acqo5._4EzTm > div > div > div.WaOAr._8E02J > div > button'
    button_advance_2 = 'body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eG' \
                       'OV_.acqo5._4EzTm > div > div > div.WaOAr._8E02J > div > button'
    browser.find_element(By.CSS_SELECTOR, button_advance_1).click()
    sleep(time_10seg_def)
    browser.find_element(By.CSS_SELECTOR, button_advance_2).click()
    sleep(time_10seg_def)


def system_copy_comment(login_def, file_comment_def):
    time_10seg_def = 10
    pyautogui.PAUSE = 5
    pyautogui.hotkey('ctrl', 'alt', 't')
    sleep(time_10seg_def)
    pyautogui.typewrite(f'cd bots_posts/{login_def}', 0.5)
    pyautogui.hotkey('enter')
    pyautogui.typewrite(f'gedit comments/{file_comment_def}', 0.5)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.typewrite('exit')
    pyautogui.hotkey('enter')


def system_comment():
    time_10seg_def = 10
    sleep(time_10seg_def)
    click_comment = 'body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.uYzeu.gIMwG > div._8' \
                    '3r9B > div > div > div > div:nth-child(2) > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > textarea'
    browser.find_element(By.CSS_SELECTOR, click_comment).click()
    pyautogui.hotkey('ctrl', 'v')


def system_click_share():
    time_10seg_def = 10
    share = 'body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.I' \
            'wRSH.eGOV_.acqo5._4EzTm > div > div > div.WaOAr._8E02J > div > button'
    browser.find_element(By.CSS_SELECTOR, share).click()
    sleep(time_10seg_def)


def system_post_full(login_def, picture_post_def, file_comment_def):
    system_click_to_post()
    system_choice_post(login_def, picture_post_def)
    system_advance()
    system_copy_comment(login_def, file_comment_def)
    system_comment()
    system_click_share()
    system_update()


def system_update():
    pyautogui.hotkey('f5')


file_post_full = f'{file_post}{item_1_picture}'
file_comment_full = f'{file_comment}{item_1_comment}'


def system_delete_files(item_1_picture_def, item_1_comment_def):
    os.remove(item_1_picture_def)
    os.remove(item_1_comment_def)


def system_close_window():
    browser.close()


system_login(login, password)
system_now_no()
for i in range(0, number_posts):
    dir_pictures = sorted(os.listdir(file_post))
    dir_comment = sorted(os.listdir(file_comment))
    item_1_picture = dir_pictures[0]
    item_1_comment = dir_comment[0]
    system_post_full(login, item_1_picture, item_1_comment)
    system_delete_files(file_post_full, file_comment_full)
    sleep(time_10seg)
system_close_window()
