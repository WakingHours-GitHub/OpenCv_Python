import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import time
from numba import jit

# 边缘检测


ptime = 0
ctime = 0


# @jit(nopython=True)
def test01():
    cap = cv.VideoCapture(0)  # 获取摄像头

    while cap.isOpened():
        isRead, img = cap.read()  # 读取当前帧图像
        if isRead:
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # shift gray pic
            img_gary_boat = cv.Canny(img_gray, 400, 100)

            dispFPS(img)


            cv.imshow("img", img)
            cv.imshow("img_gary", img_gary_boat)
            cv.waitKey(1)
    return None


# @jit(nopython=True)
def dispFPS(img):
    global ptime, ctime
    ctime = time.time()  # 获取当前时间
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv.putText(img, f"FPS:{str(int(fps))}", (0, 30), cv.FONT_ITALIC, 1, (0, 0, 255))


if __name__ == '__main__':
    test01()
