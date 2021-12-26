import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 图像平移:

# cv.warpAffine(img,M,dsize)
# img: 输入图像
# M： 2*∗3移动矩阵
# 1 0 -> x方向
# 0 1 -> y方向
# dsize: 输出图像的大小

# 练习:
img = cv.imread("../../img/dog.png")

r, c = img.shape[0:2]
M = np.float32([
    [1, 0, 50], # -> 对x轴
    [0, 1, 100] # -> 对y轴
])

res = cv.warpAffine(img, M, (r, c))
plt.imshow(res[:,:,::-1])
plt.show()

res = cv.warpAffine(img, M, (2*r, 2*c))
plt.imshow(res[:,:,::-1])
plt.show()
