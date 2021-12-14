import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# Harris角点特征提取
chessboard = cv.imread("chessboard.jpg") # 读取图像
gray = cv.cvtColor(chessboard, cv.COLOR_BAYER_RG2GRAY) # 转换成为 灰度图

gray = np.float32(gray) # 转换为浮点类型

dst = cv.cornerHarris(gray, 2, 3, 0.04) # 返回这个R矩阵






