import fun
import pyautogui
import cv2
import numpy as np

def semi_automatic():
    book_pic = cv2.imread('./pic/dungeon/book.png')
    join_pic = cv2.imread('./pic/dungeon/join_fight/join.png')
    join_num_pic = cv2.imread('./pic/dungeon/join_fight/join_num.png')
    skip_pic = cv2.imread('./pic/dungeon/event/skip.png')
    finish_pic = cv2.imread('./pic/dungeon/finish/finish.png')
    floor_sign_pic = cv2.imread('./pic/dungeon/floor/floor_sign.png')
    floor = 1
    in_floor = False
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, join_pic)[0] != False:
            pyautogui.press('enter')
            while True:
                screenshot_ready = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
                if fun.find(screenshot_ready, join_num_pic)[0] != False:
                    pyautogui.press('enter')
                    fight()
                    break
                elif fun.find(screenshot_ready, skip_pic)[0] != False:
                    event()
                    break
                else:
                    fun.sleep(1000)
        elif fun.find(screenshot, join_num_pic)[0] != False:
            fun.find_and_click(screenshot, join_num_pic)
            pyautogui.press('enter')
            fight()
        elif fun.find(screenshot, finish_pic)[0] != False:
            finish()
            break
        elif fun.find(screenshot, floor_sign_pic)[0] != False:
            if in_floor == False:
                in_floor = True
                print('第', floor, '层')
                floor += 1
        elif fun.find(screenshot, book_pic)[0] != False:
            in_floor = False
        else:
            fun.sleep(1000)


def finish():
    finish2_pic = cv2.imread('./pic/dungeon/finish/finish2.png')
    finish_reward_pic = cv2.imread('./pic/dungeon/finish/finish_reward.png')
    finish_reward2_pic = cv2.imread('./pic/dungeon/finish/finish_reward2.png')
    confirm_pic = cv2.imread('./pic/dungeon/finish/confirm.png')
    pyautogui.press('enter')
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, finish2_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, finish_reward_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, finish_reward2_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, confirm_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, confirm_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
    print('镜牢结束')

# 战斗
def fight():
    print('进入战斗')
    win_rate_pic = cv2.imread('./pic/win_rate.png')
    book = cv2.imread('./pic/dungeon/book.png')
    get_ego_pic = cv2.imread('./pic/dungeon/choose_ego/get_ego.png')
    finish_pic = cv2.imread('./pic/dungeon/finish/finish.png')
    floor_sign_pic = cv2.imread('./pic/dungeon/floor/floor_sign.png')
    turn = 1
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, win_rate_pic)[0] != False:
            pyautogui.press('p')
            fun.randomSleep(500, 1000)
            pyautogui.press('enter')
            print('回合', turn)
            turn += 1
            fun.sleep(3000)
        elif fun.find(screenshot, book)[0] != False:
            break
        elif fun.find(screenshot, get_ego_pic)[0] != False:
            break
        elif fun.find(screenshot, finish_pic)[0] != False:
            break
        elif fun.find(screenshot, floor_sign_pic)[0] != False:
            break
        else:
            fun.sleep(1000)
    print('结束战斗')

def event():
    skip_pic = cv2.imread('./pic/dungeon/event/skip.png')
    judge_pic = cv2.imread('./pic/dungeon/event/judge.png')
    continue_pic = cv2.imread('./pic/dungeon/event/continue.png')
    continue2_pic = cv2.imread('./pic/dungeon/event/continue2.png')
    choose_people_pic = cv2.imread('./pic/dungeon/event/choose_people.png')
    store_pic = cv2.imread('./pic/dungeon/store.png')
    level_up_pic = cv2.imread('./pic/dungeon/event/level_up.png')
    high_pic = cv2.imread('./pic/dungeon/event/high.png')
    determine_pic = cv2.imread('./pic/dungeon/event/determine.png')
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, choose_people_pic)[0] != False:
            fun.find_and_click(screenshot, high_pic)
            while True:
                screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
                if fun.find(screenshot, determine_pic)[0] != False:
                    fun.find_and_click(screenshot, determine_pic)
                    break
                else:
                    fun.sleep(1000)
        elif fun.find(screenshot, continue_pic)[0] != False:
            fun.find_and_click(screenshot, continue_pic)
            while True:
                screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
                fun.simulate_click()
                if fun.find(screenshot, choose_people_pic)[0] != False:
                    break
        elif fun.find(screenshot, judge_pic)[0] != False:
            if fun.find(screenshot, level_up_pic)[0] != False:
                fun.find_and_click(screenshot, level_up_pic)
            else:
                break
        elif fun.find(screenshot, store_pic)[0] != False:
            print('进入商店')
            break
        elif fun.find(screenshot, skip_pic)[0] != False:
            fun.find_and_click(screenshot, skip_pic)
        # else:
            # fun.randomSleep(300, 1000)



semi_automatic()
# fight()