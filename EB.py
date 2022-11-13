import pyautogui
import time
subject='''Issue'''
matter='''Matter ho gaya'''
name='shripad'
pyautogui.press('win')
time.sleep(2)
pyautogui.write('brave', interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('gmail.com', interval=0.1)
pyautogui.press('enter')
time.sleep(10)
pyautogui.moveTo(128,226,duration=1)
pyautogui.click()
time.sleep(1)
ne={'shripad':'babrekarmanjusha1@gmail.com',}
def ntoe():
    email=str(ne.get(name))
    pyautogui.write(email, interval=0.1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(1341,501,duration=1)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(subject, interval=0.1)
    time.sleep(2)
    pyautogui.moveTo(1159,520,duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(matter, interval=0.1)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)  
if name=='shripad':
    ntoe()



