import instaloader
import pyautogui
import time

pyautogui.PAUSE = 5

profile_name = input("Enter Insta Profile name: ")
login = input("Enter login: ")
print("Downloading Media...")
instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)
print("Download Completed!")

time.sleep(10)
pyautogui.hotkey('ctrl', 'alt', 'p')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('PycharmProjects')
pyautogui.press('down')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('system_bot')
pyautogui.press('down')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite(profile_name)
pyautogui.press('down')
pyautogui.hotkey('enter')


def delete_files(file_extension):
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite(file_extension)
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('delete')
    pyautogui.hotkey('alt', 'left')


delete_files('.json.xz')
time.sleep(5)
delete_files('.txt')
time.sleep(5)
delete_files('id')
time.sleep(5)
delete_files('data')
time.sleep(5)
delete_files('profile')
