import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# 霍夫线检测
# 原理, 涉及霍夫空间变换, 和极坐标的霍夫空间变换
# 先边缘检测, 然后将像素点, 映射到霍夫空间(r和theta坐标轴).
# 创建一个二维的累加矩阵, 分别是r,和theta
# 然后对于每个点, 再霍夫空间上遍历theta,然后r是从0到图像的对角线长度, 如果扫到点了
# 我们就在累加矩阵上累加数,
# 遍历完所有的点后, 矩阵上数最大的就是直线对应的r和theta, 这由HoughLine()返回一个列表

rili = cv.imread("rili.jpg")
rili_gray = cv.cvtColor(rili, cv.COLOR_BGR2GRAY)

rili_gray_edge = cv.Canny(rili_gray, 46, 60)

lines = cv.HoughLines(rili_gray_edge, 0.8, np.pi/180, 150)
for line in lines:
    rho, theta = line[0] # 拿到每个rho和theta
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = rho * a
    y0 = rho * b

    # x1 =
    




















