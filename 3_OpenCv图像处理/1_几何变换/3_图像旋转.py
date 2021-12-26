import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 图像旋转:
# 原理: 首先找到数学关系:
# 利用参数方程 ->
# 然后调整位置

# 获取M矩阵:
# cv2.getRotationMatrix2D(center, angle, scale)
# 参数：
# center：旋转中心
# angle：旋转角度
# scale：缩放比例
# return 返回变换M矩阵

# 然后使用warpAffine()进行变换

# 练习:
img = cv.imread("../../img/dog.png")

r, c = img.shape[0:2]
M = cv.getRotationMatrix2D((r/2, c/2), 45, 0.5)

res = cv.warpAffine(img, M, (r, c))

plt.imshow(res[:,:,::-1])
plt.show() # 这样图像就被旋转了45度







































