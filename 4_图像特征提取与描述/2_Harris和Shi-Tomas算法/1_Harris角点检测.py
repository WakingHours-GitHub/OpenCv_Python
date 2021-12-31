import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

"""
图像特征
图像特征要有区分性，容易被比较。一般认为角点，斑点等是较好的图像特征
特征检测：找到图像中的特征
特征描述：对特征及其周围的区域进行描述

而角点特征: 是图像特征的一种

焦点检测的一个基本原理:
Harris角点检测的思想是通过图像的局部的小窗口观察图像，角点的特征是窗口沿任意方向移动都会导致图像灰度的明显变化，如下图所示：
所以我们只需要找出局部窗口向各个方向移动后的灰度差值的总和.


Harris焦点检测原理:
E(u,v) = sum(w(x,y),[I(x+u, y+v) - I(x, y)]^2 )
其中: I(x,y)是局部窗口的图像灰度, 而I(x+u, y+v)是移动后局部窗口的图像灰度
w(x,y)是窗口函数, 可以是矩形窗口, 也可也是赋予窗口中的像素的不同权重的高斯窗口.

对于公式.泰勒展开:
E(u,v) = [u, v] M [u, v]' # '表示转至
M = sum(w(x, y) [Ix2 IxIy; IxIy Iy2]    
显然, M矩阵决定了E(u, v)的取值, 下面我们利用M求取角点
M中是由Ix2和Iy2决定的. 所以有韦达公式
得到lambda_max, 和lambda_min

但是Harris中给出的焦点检测是: R = detM - a(traceM)^2
其中, detM为M的行列式, traceM为矩阵M的迹, a为常数


"""

# Harris角点特征提取
# API:
# dst=cv.cornerHarris(src, blockSize, ksize, k)
# img：数据类型为 ﬂoat32 的输入图像。
# blockSize：角点检测中要考虑的邻域大小。
# ksize：sobel求导使用的核大小.
# k ：角点检测方程中的自由参数，取值参数为 [0.04，0.06]. 就是a
# return: 返回的是一个记矩阵


chessboard = cv.imread("chessboard.jpg")  # 读取图像
gray = cv.cvtColor(chessboard, cv.COLOR_BGR2GRAY)  # 转换成为 灰度图

gray = np.float32(gray)  # 转换为浮点类型, 转换为float32类型

dst = cv.cornerHarris(gray, 2, 3, 0.04)  # 返回这个R矩阵
# 返回的dst = R = l1l2 - k(l1+l2)^2
# 所以dst.max()返回的就是那个灰度变化最大的点, 也就是最角点的那个角点,
# 然后我们下放[阈值], 对其他焦点进行检测, 返回逻辑数组, 对其进行检测
# 用灰度图进行检测, 然后检测的结果花在原图上
print(dst.max())
print(dst >= 0.001 * dst.max())
chessboard[dst > 0.01 * dst.max()] = (0, 0, 255)

plt.imshow(chessboard[:, :, ::-1])
plt.show()

# 练习:
if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while True:
        isOpen, img = cap.read()
        # 全是红色的, 不清楚为什么
        if isOpen:
            img_64 = np.float32(img)
            img_64_gray = cv.cvtColor(img_64, cv.COLOR_BGR2GRAY)
            r = cv.cornerHarris(img_64_gray, 2, 3, 0.04) #
            # 参数分别是, img_gray, 邻域, Sobel算子核大小, K参数
            img[r > 0.9 * r] = [0, 0, 255]

            cv.imshow("img", img)
            cv.waitKey(1)
