import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



# 边缘检测


cap = cv.VideoCapture(0) # 获取摄像头

while cap.isOpened():
    isRead, img = cap.read() # 读取当前帧图像
    if isRead:
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # shift gray pic
        img_gary_boat = cv.Canny(img, 10, 100)



        # cv.imshow("img", img)
        cv.imshow("img_gary", img_gary_boat)
        cv.waitKey(1)



