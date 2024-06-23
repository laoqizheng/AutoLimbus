import fun
import pyautogui
import cv2
import numpy as np
import time
import math

win_rate_pic = cv2.imread('./pic/win_rate.png')
book_pic = cv2.imread('./pic/dungeon/book.png')
get_ego_pic = cv2.imread('./pic/dungeon/choose_ego/get_ego.png')
finish_pic = cv2.imread('./pic/dungeon/finish/finish.png')
floor_sign_pic = cv2.imread('./pic/dungeon/floor/floor_sign.png')
skip_pic = cv2.imread('./pic/dungeon/event/skip.png')
judge_pic = cv2.imread('./pic/dungeon/event/judge.png')
continue_pic = cv2.imread('./pic/dungeon/event/continue.png')
continue2_pic = cv2.imread('./pic/dungeon/event/continue2.png')
choose_people_pic = cv2.imread('./pic/dungeon/event/choose_people.png')
store_pic = cv2.imread('./pic/dungeon/store.png')
level_up_pic = cv2.imread('./pic/dungeon/event/level_up.png')
normal_ego_pic = cv2.imread('./pic/dungeon/event/normal_ego.png')  # 泛用ego

extremely_high_pic = cv2.imread('pic/dungeon/event/extremely_high.png')  # 极高
high_pic = cv2.imread('pic/dungeon/event/high.png')  # 高
determine_pic = cv2.imread('./pic/dungeon/event/determine.png')
join_pic = cv2.imread('./pic/dungeon/join_fight/join.png')
join_num_pic = cv2.imread('./pic/dungeon/join_fight/join_num.png')

battle_num = 0

def semi_automatic():
    floor = 1
    in_floor = False
    start_time = time.time()
    global battle_num
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, join_pic)[0] != False:
            pyautogui.press('enter')
            while True:
                screenshot_ready = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
                if fun.find(screenshot_ready, join_num_pic)[0] != False:
                    pyautogui.press('enter')
                    battle_num += 1
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
            battle_num += 1
            fight()
        elif fun.find(screenshot, finish_pic)[0] != False:
            spend_seconds = math.floor(time.time() - start_time)
            print('镜牢结束')
            print('战斗场次', battle_num)
            print('总耗时', math.floor(spend_seconds / 60), '分', math.floor(spend_seconds) % 60, '秒')
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
    fun.sleep(1000)
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, finish_reward_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
    fun.sleep(1000)
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, finish_reward2_pic)[0] != False:
            pyautogui.press('enter')
            break
        else:
            fun.sleep(1000)
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


# 战斗
def fight():
    print('进入战斗')
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
        elif fun.find(screenshot, book_pic)[0]:
            break
        elif fun.find(screenshot, get_ego_pic)[0]:
            break
        elif fun.find(screenshot, finish_pic)[0]:
            break
        elif fun.find(screenshot, floor_sign_pic)[0]:
            break
        else:
            fun.sleep(1000)
    print('结束战斗')


def event():
    global battle_num
    confirm_pic = cv2.imread('./pic/dungeon/event/confirm.png')
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, judge_pic)[0]:
            fun.sleep(1000)
            ego_event_choose()
        elif fun.find(screenshot, continue_pic)[0]:
            fun.find_and_click(screenshot, continue_pic)
            fun.sleep(1000)
        elif fun.find(screenshot, choose_people_pic)[0]:
            if fun.find(screenshot, extremely_high_pic)[0]:
                fun.find_and_click(screenshot, extremely_high_pic)
            elif fun.find(screenshot, high_pic)[0]:
                fun.find_and_click(screenshot, high_pic)
        elif fun.find(screenshot, determine_pic)[0]:
            fun.find_and_click(screenshot, determine_pic)
        elif fun.find(screenshot, store_pic)[0]:
            print('进入商店')
            break
        elif fun.find(screenshot, skip_pic)[0]:
            fun.find_and_click(screenshot, skip_pic)
        elif fun.find(screenshot, confirm_pic)[0]:
            fun.find_and_click(screenshot, confirm_pic)
            fun.sleep(2000)
            screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
            if fun.find(screenshot, confirm_pic)[0]:
                fun.find_and_click(screenshot, confirm_pic)
            break
        elif fun.find(screenshot, join_num_pic)[0]:
            pyautogui.press('enter')
            fight()
            battle_num += 1
            break
        elif fun.find(screenshot, book_pic)[0]:
            break
        else:
            fun.simulate_click()
            pass


def ego_event_order():
    return [
        {'index': 1, 'label': '等级'},
        {'index': 2, 'label': '流血E.G.0'},
        {'index': 3, 'label': '呼吸E.G.0'},
        {'index': 4, 'label': '泛用E.G.0'},
        # {'index': 5, 'label': '充能E.G.0'},
        {'index': 6, 'label': 'E.G.0'},
    ]


def ego_event_choose():
    arr = ego_event_order()
    option1_loc = ((1400, 360), (2300, 560))
    option2_loc = ((1400, 610), (2300, 810))
    option3_loc = ((1400, 860), (2300, 1060))
    option1 = fun.get_text(option1_loc[0][0], option1_loc[0][1], option1_loc[1][0] - option1_loc[0][0], option1_loc[1][1] - option1_loc[0][1])
    option1_level = 99
    if option1:
        for i in arr:
            if i['label'] in option1:
                option1_level = i['index']
    option2 = fun.get_text(option2_loc[0][0], option2_loc[0][1], option2_loc[1][0] - option2_loc[0][0], option2_loc[1][1] - option2_loc[0][1])
    option2_level = 99
    if option2:
        for i in arr:
            if i['label'] in option2:
                option2_level = i['index']
    option3 = fun.get_text(option3_loc[0][0], option3_loc[0][1], option3_loc[1][0] - option3_loc[0][0], option3_loc[1][1] - option3_loc[0][1])
    option3_level = 99
    if option3:
        for i in arr:
            if i['label'] in option3:
                option3_level = i['index']
    tup1 = (0, 0)
    tup2 = (0, 0)
    if option1_level <= option2_level and option1_level <= option3_level:
        tup1, tup2 = option1_loc[0], option1_loc[1]
    elif option2_level <= option2_level and option2_level <= option3_level:
        tup1, tup2 = option2_loc[0], option2_loc[1]
    elif option3_level <= option1_level and option3_level <= option2_level:
        tup1, tup2 = option3_loc[0], option3_loc[1]
    fun.simulate_move(tup1, tup2)
    fun.randomSleep(300, 1000)
    fun.simulate_click()


# event()
semi_automatic()
