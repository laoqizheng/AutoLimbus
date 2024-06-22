import pyautogui
import cv2
import time
import random
import numpy as np

# 图像识别
def find(template, img):
    res = cv2.matchTemplate(template, img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    if loc[0].size > 0:
        h, w = img.shape[:2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        return top_left, bottom_right
    else:
        return False, False
    # cv2.imshow('res', cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2))
    # cv2.waitKey(0)

# 随机休眠
def randomSleep(min, max):
    sleep_num = random.randint(min, max) / 1000
    # print('休眠时间', sleep_num, '秒')
    time.sleep(sleep_num)

# 休眠
def sleep(num):
    time.sleep(num / 1000)

# 模拟鼠标移动
def simulate_move(tup1, tup2):
    pyautogui.moveTo(random.randint(tup1[0], tup2[0]), random.randint(tup1[1], tup2[1]))

# 模拟鼠标点击
def simulate_click():
    pyautogui.click()

# 识别图片并点击
def find_and_click(template, img, min_sleep = 500, max_sleep = 1000):
    tup1, tup2 = find(template, img)
    if tup1 == False:
        print('第一次识别失败')
        sleep(2000)
        tup1, tup2 = find(template, img)
    simulate_move(tup1, tup2)
    randomSleep(min_sleep, max_sleep)
    simulate_click()

# 自动镜牢
# def auto():
#     main = cv2.imread('./pic/main.png')
#     drive = cv2.imread('./pic/drive.png')
#     find(main, drive)

# 选择ego
def choose_ego():
    print('选择ego')
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    get_ego_pic = cv2.imread('./pic/get_ego.png')
    choose_ego_pic = cv2.imread('./pic/choose_ego.png')
    confirm = cv2.imread('./pic/confirm.png')
    tup1, tup2 = find(tem, get_ego_pic)
    if tup1 == False:
        return
    tup1 = (tup1[0] - 250, tup1[1] + 40)
    tup2 = (tup2[0], tup2[1] + 700)
    simulate_move(tup1, tup2)
    randomSleep(300, 1000)
    simulate_click()
    randomSleep(300, 1000)
    find_and_click(tem, choose_ego_pic)
    randomSleep(1000, 2000)
    screenshot2 = pyautogui.screenshot()
    tem2 = cv2.cvtColor(np.array(screenshot2), cv2.COLOR_BGR2RGB)
    find_and_click(tem2, confirm)


# 选择遭遇战奖励卡
def choose_reward():
    print('选择遭遇战奖励卡')
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    confirm_pic = cv2.imread('./pic/choose_reward/confirm.png')
    confirm2_pic = cv2.imread('./pic/choose_reward/confirm2.png')
    tup1 = (1200, 450)
    tup2 = (1450, 900)
    simulate_move(tup1, tup2)
    randomSleep(300, 1000)
    simulate_click()

    randomSleep(1000, 2000)
    find_and_click(tem, confirm_pic)

    while True:
        sleep(1000)
        screenshot = pyautogui.screenshot()
        tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        if find(tem, confirm2_pic)[0] != False:
            find_and_click(tem, confirm2_pic)
            break


# 进入战斗
def join_fight():
    print('进入')
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    join_pic = cv2.imread('./pic/join_fight/join.png')
    join_people = cv2.imread('./pic/join_fight/join_people.png')
    randomSleep(300, 1000)
    find_and_click(tem, join_pic)
    while True:
        sleep(1000)
        screenshot = pyautogui.screenshot()
        tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        tup1, tup2 = find(tem, join_people)
        if tup1 != False:
            tup1 = (tup1[0], tup1[1] + 180)
            tup2 = (tup2[0], tup2[1] + 230)
            simulate_move(tup1, tup2)
            randomSleep(500, 1000)
            simulate_click()
            print('开始战斗')
            break


# 结束镜牢
def finish():
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    confirm_pic = cv2.imread('./pic/finish/confirm.png')
    get_pic = cv2.imread('./pic/finish/get.png')
    confirm2_pic = cv2.imread('./pic/finish/confirm2.png')
    confirm3_pic = cv2.imread('./pic/finish/confirm3.png')
    confirm4_pic = cv2.imread('./pic/finish/confirm4.png')
    randomSleep(1000, 2000)
    find_and_click(tem, confirm_pic)
    randomSleep(1000, 2000)
    simulate_click()

    randomSleep(1000, 2000)
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    find_and_click(tem, get_pic)

    randomSleep(1000, 2000)
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    find_and_click(tem, confirm2_pic)

    randomSleep(2000, 3000)
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    find_and_click(tem, confirm3_pic)

    randomSleep(2000, 3000)
    screenshot = pyautogui.screenshot()
    tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    find_and_click(tem, confirm4_pic)

    print('结束镜牢')

# 自动战斗
def fight():
    win_rate = cv2.imread('./pic/win_rate.png')
    go = cv2.imread('./pic/go.png')
    max = cv2.imread('./pic/max.png')
    book = cv2.imread('./pic/book.png')
    get_ego = cv2.imread('./pic/get_ego.png')
    choose_reward_pic = cv2.imread('./pic/choose_reward/choose_reward.png')
    win_pic = cv2.imread('./pic/finish/win.png')
    join_pic = cv2.imread('./pic/join_fight/join.png')
    card_pic = cv2.imread('./pic/choose_card/card.png')

    turn = 1
    # 战斗状态
    fight_status = False
    # 选择卡包状态
    choose_card_status = False
    while True:
        screenshot = pyautogui.screenshot()
        tem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        res1 = find(tem, book)[0]
        res2 = find(tem, max)[0]
        res3 = find(tem, get_ego)[0]
        res4 = find(tem, choose_reward_pic)[0]
        res5 = find(tem, win_pic)[0]
        res6 = find(tem, join_pic)[0]
        res7 = find(tem, card_pic)[0]
        # print('res1', res1)
        # print('res2', res2)
        # print('res3', res4)
        # print('res4', res4)
        # print('res5', res5)
        # print('res6', res6)
        if res6 != False:
            join_fight()
        elif res1 != False:
            continue
        elif res2 != False:
            fight_status = True
            find_and_click(tem, win_rate)
            randomSleep(300, 1000)
            find_and_click(tem, go)
            print('回合', turn)
            turn += 1
            sleep(4000)
        elif res3 != False:
            if fight_status == True:
                fight_status = False
                turn = 1
                print('战斗结束')
            choose_ego()
        elif res4 != False:
            if fight_status == True:
                fight_status = False
                turn = 1
                print('战斗结束')
            choose_reward()
        elif res5 != False:
            finish()
        elif res7 != False:
            if choose_card_status == False:
                print('选择主题卡包')
                choose_card_status = True
        else:
            sleep(1000)

# main = cv2.imread('./pic/main.png')
# drive = cv2.imread('./pic/drive.png')
# find_and_click(main, drive)

# fight()
# choose_reward()