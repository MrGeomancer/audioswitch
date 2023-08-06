import pyautogui
import time
def switch():
    # pyautogui.confirm(text='', title='', buttons=['вклюяить', 'Выключить'])
    pos = pyautogui.position()
    pyautogui.moveTo(1730, 1065, 0.15)
    # pyautogui.moveTo(1730, 1065)
    pyautogui.click(1730, 1065, button='right')
    pyautogui.click(1730, 1010)
    time.sleep(0.3)
    soundwindow = pyautogui.locateOnScreen(r'png\soundwindow.png',confidence=0.8)
    # print(soundwindow)
    if soundwindow == None:
        soundwindow = pyautogui.locateOnScreen(r'png\soundwindow.png',confidence=0.8)
        # print(soundwindow)
    pyautogui.click(soundwindow[0]+10, soundwindow[1]+45)
    time.sleep(0.2)
    speaker_on = pyautogui.locateOnScreen(r'png\\speakeron.png',confidence=0.95)
    if speaker_on != None:
        pyautogui.click(pyautogui.center(speaker_on), button='right')
        pyautogui.click(speaker_on[0]+50, speaker_on[1]+75)
    else:
        pyautogui.click(soundwindow[0]+100, soundwindow[1]+100, button='right')
        pyautogui.click(soundwindow[0] + 150, soundwindow[1] + 140)
        # pyautogui.click(speaker_on[0] + 50, speaker_on[1] + 75)
    pyautogui.click(soundwindow[0] + 440, soundwindow[1] + 5)
    pyautogui.moveTo(pos)
    # pyautogui.moveTo(150, 150, 0.15)
    # pyautogui.click()
    # speaker = pyautogui.locateOnScreen('speakeroff.png')
if __name__ == '__main__':
    switch()
#1732 1067
