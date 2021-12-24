"""
Open-Cv:
图像处理库

图像是什么：
图是物体反射或者投射光的分布。像是人的视觉系统在人脑中所形成的认识或者印象。

数字图像的表示：
0表示黑，1表示白

图像的分类：
二值图像：仅有0，1表示,不是白色就是黑色
灰度图：每个像素只有一个采样的图像，256级灰度
彩色图：有红(R),绿(G),蓝(B)三个分量来表示的.




"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/matplot_py.png")

plt.imshow(img[:, :, ::-1])
plt.show()

# cv.imshow("imd", img)
#
# cv.waitKey(0)
