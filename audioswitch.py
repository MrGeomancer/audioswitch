import pyautogui
import time
import traceback


def switch():  # выполняемая функция
    # запомнить начальную позицию мыши, чтобы потом вернуть её туда
    start_mouse_position = pyautogui.position()
    # нажать пкм по причному расположению динамиков через 0,15 секунд после прошлого действия
    pyautogui.click(1730, 1065, button='right', duration=0.15)
    # нажать на "звуки"
    pyautogui.click(1730, 1010)
    # подождать 0,3 секунды до появления окна звуков
    time.sleep(0.33)
    # найти на всём экране расположения окна звуков
    soundwindow = pyautogui.locateOnScreen(r'png\soundwindow.png', confidence=0.8)

    if soundwindow == None:  # в случае если он не нашел, попробует еще раз
        soundwindow = pyautogui.locateOnScreen(r'png\soundwindow.png', confidence=0.8)

    # открыть окно "воспроизведения"
    pyautogui.click(soundwindow[0] + 10, soundwindow[1] + 45)
    # подождать 0,2 секунды прогрузки
    time.sleep(0.2)
    # найти иконку включенных динамиков
    try:
        speaker_on = pyautogui.locateOnScreen(r'png\\speakeron.png', confidence=0.95)
    except pyautogui.ImageNotFoundException as e:
        speaker_on = None

    if speaker_on is not None:  # если икона включенных динамиков есть, то:
        pyautogui.click(pyautogui.center(speaker_on), button='right')  # нажать по ней ПКМ
        pyautogui.click(speaker_on[0] + 50, speaker_on[1] + 75)  # нажать "Отключить"
    else:  # если иконки нет
        pyautogui.click(soundwindow[0] + 100, soundwindow[1] + 100, button='right')  # нажать пкм по первому устройсву
        pyautogui.click(soundwindow[0] + 150, soundwindow[1] + 140)  # включить его
    # нажать на кнопку закрытия окна
    pyautogui.click(soundwindow[0] + 440, soundwindow[1] + 5)
    # вернуть курсор на начальную позицию
    pyautogui.moveTo(start_mouse_position)


if __name__ == '__main__':
    try:
        switch()
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
# 1732 1067
