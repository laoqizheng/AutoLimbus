import fun
import pyautogui
import cv2
import numpy as np
import time
import math
import random
import config

win_rate_pic = cv2.imread('./pic/win_rate.png')
book_pic = cv2.imread('./pic/dungeon/book.png')
get_ego_pic = cv2.imread('./pic/dungeon/choose_ego/get_ego.png')
choose_reward_pic = cv2.imread('./pic/dungeon/choose_reward/choose_reward.png')
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
normal_pic = cv2.imread('pic/dungeon/event/normal.png')  # 一般
determine_pic = cv2.imread('./pic/dungeon/event/determine.png')
join_pic = cv2.imread('./pic/dungeon/join_fight/join.png')
join_num_pic = cv2.imread('./pic/dungeon/join_fight/join_num.png')
fight_pic = cv2.imread('./pic/dungeon/event/fight.png')
leave_pic = cv2.imread('./pic/dungeon/store/leave.png')
confirm_leave_rest_pic = cv2.imread('pic/dungeon/store/confirm_leave_rest.png')
confirm_leave_store_pic = cv2.imread('./pic/dungeon/store/confirm_leave_store.png')

battle_num = 0
last_pos = 2
floor = 1

def semi_automatic():
    in_floor = False
    in_reward = False
    in_ego = False
    start_time = time.time()
    global battle_num
    while True:
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, join_pic)[0]:
            pyautogui.press('enter')
            while True:
                screenshot_ready = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
                if fun.find(screenshot_ready, join_num_pic)[0]:
                    pyautogui.press('enter')
                    battle_num += 1
                    fight()
                    break
                elif fun.find(screenshot_ready, skip_pic)[0]:
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
                global last_pos
                global floor
                if floor != 1:
                    last_pos = 'boss'
                in_floor = True
                print('第', floor, '层')
                floor += 1
                fun.sleep(2000)
                if config.auto_choose_card:
                    choose_card()
        elif fun.find(screenshot, get_ego_pic)[0]:
            if in_ego == False:
                print('选择ego')
                in_ego = True
                choose_ego()
        elif fun.find(screenshot, choose_reward_pic)[0]:
            if in_reward == False:
                print('选择遭遇战奖励')
                in_reward = True
                choose_reward()
        elif fun.find(screenshot, book_pic)[0]:
            in_floor = False
            in_reward = False
            in_ego = False
            next_ele()
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
            fun.sleep(5000)
        elif fun.find(screenshot, book_pic)[0]:
            break
        elif fun.find(screenshot, get_ego_pic)[0]:
            break
        elif fun.find(screenshot, choose_reward_pic)[0]:
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
            elif fun.find(screenshot, normal_pic)[0]:
                fun.find_and_click(screenshot, normal_pic)
            fun.sleep(1000)
        elif fun.find(screenshot, determine_pic)[0]:
            fun.find_and_click(screenshot, determine_pic)
            fun.sleep(1000)
        elif fun.find(screenshot, store_pic)[0]:
            print('进入商店')
            if config.auto_skip_store:
                fun.sleep(2000)
                fun.find_and_click(screenshot, leave_pic)
                store_confirm_pic = cv2.imread('./pic/dungeon/store/confirm.png')
                while True:
                    screenshot = fun.screenshot()
                    if fun.find(screenshot, confirm_leave_store_pic)[0]:
                        print('leave_store')
                        fun.find_and_click(screenshot, store_confirm_pic)
                        # a, b = fun.find(screenshot, confirm_leave_store_pic)
                        # cv2.imshow('res', cv2.rectangle(screenshot, a, b, (0, 255, 0), 2))
                        # cv2.waitKey(0)
                        break
                    elif fun.find(screenshot, confirm_leave_rest_pic)[0]:
                        print('leave_rest')
                        fun.find_and_click(screenshot, store_confirm_pic)
                        break
                    else:
                        print('sleep')
                        fun.sleep(1000)
            break
        elif fun.find(screenshot, fight_pic)[0]:
            fun.find_and_click(screenshot, fight_pic)
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
        {'index': 5, 'label': 'E.G.0'},
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


def next_ele():
    global last_pos
    loc_list = [
        (1370, 60),
        (1370, 490),
        (1370, 920)
    ]
    can_go_list = [
        (1370, 60),
        (1370, 490),
        (1370, 920)
    ]
    if last_pos == 1 or last_pos == 3:
        can_go_list.pop(last_pos - 1)
    elif last_pos == 'boss':
        can_go_list = [(1370, 490)]
    length = 160
    for i in can_go_list:
        fun.simulate_move(i, (i[0] + length, i[1] + length))
        fun.randomSleep(500, 1000)
        fun.simulate_click()
        fun.sleep(1000)
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot, join_pic)[0]:
            if last_pos == 'boss':
                last_pos = 2
            else:
                last_pos = last_pos + loc_list.index(i) - 1
            break


def choose_reward():
    confirm_pic = cv2.imread('./pic/dungeon/choose_reward/confirm.png')
    confirm2_pic = cv2.imread('./pic/dungeon/choose_reward/confirm2.png')
    get_ego_pic = cv2.imread('./pic/dungeon/choose_reward/get_ego.png')
    # 3 4
    arr = [
        {'index': 1, 'label': 'E.G.0'},
        {'index': 2, 'label': '经费'},
        {'index': 3, 'label': '星光'}
    ]
    options = [
        {'loc': (760, 690), 'index': 99},
        {'loc': (1170, 690), 'index': 99},
        {'loc': (1580, 690), 'index': 99}
    ]
    length = 300
    width = 200
    for i in options:
        text = fun.get_text(i['loc'][0], i['loc'][1], length, width)
        for j in arr:
            if j['label'] in text:
                i['index'] = j['index']
                break
    options.sort(key = lambda i:i['index'])
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
    tup1 = options[0]['loc']
    tup2 = (tup1[0] + length, tup1[1] + width)
    fun.simulate_move(tup1, tup2)
    fun.randomSleep(300, 1000)
    fun.simulate_click()
    fun.sleep(1000)
    fun.find_and_click(screenshot, confirm_pic)
    fun.sleep(1000)
    if options[0]['index'] == 1:
        while True:
            screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
            if fun.find(screenshot, get_ego_pic)[0]:
                fun.find_and_click(screenshot, confirm2_pic)
                break
            elif fun.find(screenshot, book_pic)[0]:
                break
            elif fun.find(screenshot, floor_sign_pic)[0]:
                break
            else:
                fun.sleep(1000)
    fun.sleep(2000)


def choose_ego():
    confirm_pic = cv2.imread('./pic/dungeon/choose_ego/confirm.png')
    fun.simulate_move((1055, 350), (1504, 1064))
    fun.randomSleep(300, 1000)
    fun.simulate_click()
    fun.sleep(1000)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
    fun.find_and_click(screenshot, get_ego_pic)
    fun.sleep(1000)
    num = 1
    while True:
        screenshot2 = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        if fun.find(screenshot2, confirm_pic)[0]:
            fun.find_and_click(screenshot2, confirm_pic)
            break
        else:
            fun.sleep(1000)
        num += 1


def choose_card():
    tup1 = (275, 485)
    tup2 = (607, 825)
    x = random.randint(tup1[0], tup2[0])
    y = random.randint(tup1[1], tup2[1])
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x, y+500, 1, button='left')


# choose_reward()
semi_automatic()