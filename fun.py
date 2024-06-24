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



# 打印模块数
def print_module():
    module_pic = cv2.imread('pic/module.png')
    template = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
    tup1, tup2 = find(template, module_pic)
    module_num_pic = pyautogui.screenshot(region=[tup2[0], tup1[1], 100, tup2[1] - tup1[1]])
    print('模块', pytesseract.image_to_string(module_num_pic, lang='chi_sim').replace('\n', ''))


def get_text(x, y, length, width):
    img = pyautogui.screenshot(region=[x, y, length, width])
    # cv2.imshow('res', cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
    # cv2.waitKey(0)
    return pytesseract.image_to_string(img, lang='chi_sim').replace('\n', '')


def screenshot():
    return cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)




# a, b = find(cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB), cv2.imread('./pic/aa.png'))
# img = pyautogui.screenshot(region=[2170, 916, 247, 51])
# cv2.imshow('a', cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
# a, b = find(screenshot(), cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
# print(a)
# print(b)
# print(get_text(a[0], a[1], b[0] - a[0], b[1] - a[1]))
# cv2.imshow('res', cv2.rectangle(tem, a, b, (0, 255, 0), 2))
# cv2.waitKey(0)
