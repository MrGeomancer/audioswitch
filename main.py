import pyautogui
def switch():
    # pyautogui.confirm(text='', title='', buttons=['вклюяить', 'Выключить'])
    pyautogui.moveTo(1730, 1065, 0.15)
    # pyautogui.moveTo(1730, 1065)
    pyautogui.click(1730, 1065, button='right')
    pyautogui.moveTo(1730, 1010)
    pyautogui.click()
    # soundwindow = pyautogui.locateOnScreen('png\\soundwindow.png', confidence=0.9)
    # soundwindow
    pyautogui.locateOnScreen('png\soundwindow.png')
    print('hh')
    # pyautogui.moveTo(150, 150, 0.15)
    # pyautogui.click()
    # speaker = pyautogui.locateOnScreen('speakeroff.png')
if __name__ == '__main__':
    switch()
#1732 1067
