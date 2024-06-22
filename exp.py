import math
import time
import fun
import pyautogui
import cv2
import numpy as np

# 经验本
def go_exp(num = 1):
    start_time = time.time()
    current = 1
    while current <= num:
        screenshot = pyautogui.screenshot()
        template = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        drive_pic = cv2.imread('./pic/drive.png')
        exp_logo_pic = cv2.imread('./pic/exp/exp_logo.png')
        exp_6_pic = cv2.imread('./pic/exp/exp_6.png')
        if fun.find(template, exp_6_pic)[0] != False:
            exp_6 = cv2.imread('./pic/exp/exp_6.png')
            loc1, loc2 = fun.find(template, exp_6)
            screenshot_exp_6 = pyautogui.screenshot(region=[loc1[0], loc1[1], loc2[0], loc2[1]])
            template_exp_6 = cv2.cvtColor(np.array(screenshot_exp_6), cv2.COLOR_BGR2RGB)
            join_pic = cv2.imread('./pic/exp/join.png')
            loc3, loc4 = fun.find(template_exp_6, join_pic)
            fun.simulate_move((loc1[0] + loc3[0], loc1[1] + loc3[1]), (loc1[0] + loc4[0], loc1[1] + loc4[1]))
            fun.randomSleep(500, 1000)
            fun.simulate_click()
            while True:
                screenshot_ready = pyautogui.screenshot()
                template_ready = cv2.cvtColor(np.array(screenshot_ready), cv2.COLOR_BGR2RGB)
                join_num_pic = cv2.imread('./pic/exp/join_num.png')
                if fun.find(template_ready, join_num_pic)[0] != False:
                    pyautogui.press('enter')
                    break
                else:
                    fun.sleep(1000)
            print('第', current, '次战斗')
            fight()
            current += 1
        elif fun.find(template, exp_logo_pic)[0] != False:
            fun.find_and_click(template, exp_logo_pic)
        elif fun.find(template, drive_pic)[0] != False:
            fun.find_and_click(template, drive_pic)
        else:
            fun.sleep(1000)
    spend_seconds = math.floor(time.time() - start_time)
    print('-------------')
    print('战斗场次', num)
    print('总耗时', math.floor(spend_seconds / 60), '分', math.floor(spend_seconds) % 60, '秒')

# 战斗
def fight():
    win_rate = cv2.imread('./pic/win_rate.png')
    win_pic = cv2.imread('./pic/exp/win.png')
    lose_pic = cv2.imread('./pic/exp/lose.png')
    turn = 1
    while True:
        screenshot = pyautogui.screenshot()
        template = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        if fun.find(template, win_rate)[0] != False:
            pyautogui.press('p')
            fun.randomSleep(500, 1000)
            pyautogui.press('enter')
            print('回合', turn)
            turn += 1
            fun.sleep(3000)
        elif fun.find(template, win_pic)[0] != False:
            print('战斗胜利')
            pyautogui.press('enter')
            fun.simulate_move((0, 0), (500, 500))
            return
        elif fun.find(template, lose_pic)[0] != False:
            print('战斗失败')
            pyautogui.press('enter')
            fun.simulate_move((0, 0), (500, 500))
            return
        else:
            fun.sleep(1000)


def get_module():
    print('模块数：')


go_exp(2)