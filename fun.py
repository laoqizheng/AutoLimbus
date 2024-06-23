import pyautogui
import cv2
import time
import random
import numpy as np
import pytesseract
from PIL import Image


# 图像识别
def find(template, img):
    res = cv2.matchTemplate(template, img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
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
def find_and_click(template, img, min_sleep=500, max_sleep=1000):
    tup1, tup2 = find(template, img)
    if tup1 == False:
        print('第一次识别失败')
        sleep(2000)
        tup1, tup2 = find(template, img)
    simulate_move(tup1, tup2)
    randomSleep(min_sleep, max_sleep)
    simulate_click()


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


# 打印模块数
def print_module():
    module_pic = cv2.imread('pic/module.png')
    template = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
    tup1, tup2 = find(template, module_pic)
    module_num_pic = pyautogui.screenshot(region=[tup2[0], tup1[1], 100, tup2[1] - tup1[1]])
    print('模块', pytesseract.image_to_string(module_num_pic, lang='chi_sim').replace('\n', ''))


def get_text(x, y, length, width):
    img = pyautogui.screenshot(region=[x, y, length, width])
    return pytesseract.image_to_string(img, lang='chi_sim').replace('\n', '')


