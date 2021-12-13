import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 腐蚀 -> 高亮区域被蚕食, 是局部最大值的操作
# 具体操作是：用一个结构元素扫描图像中的每一个像素，
# 用结构元素中的每一个像素与其覆盖的像素做“与”操作，
# 如果都为1，则该像素为1，否则为0。
# 腐蚀的作用是消除物体边界点，使目标缩小，可以消除小于结构元素的噪声点。
# API:

# cv.erode(img, kernel, iterations)
# img: 要处理的图像
# kernel: 核结构
# iterations: 腐蚀的次数，默认是1

# 膨胀
# 具体操作是：用一个结构元素扫描图像中的每一个像素，
# 用结构元素中的每一个像素与其覆盖的像素做“与”操作，
# 如果都为0，则该像素为0，否则为1。
# API:

# cv.dilate(img, kernel, iterations)
# img: 要处理的图像
# kernel: 核结构
# iterations: 腐蚀的次数，默认是1

# 练习:
img = cv.imread("letter.png")
# plt.figure(1)
plt.imshow(img[:, :, ::-1])
plt.show()
# 创建kernel结构:
kernel = np.ones((5, 5), np.uint8)
"""
kernel:
    1   1   1   1   1
    1   1   1   1   1
    1   1   1   1   1
    1   1   1   1   1
    1   1   1   1   1
    
"""
# 图像腐蚀和膨胀
fushi_img = cv.erode(img, kernel)  # 腐蚀
# plt.figure(2)
plt.imshow(fushi_img[:, :, ::-1])
plt.show()

pengzhang_img = cv.dilate(img, kernel)
# plt.figure(3)
plt.imshow(pengzhang_img[:, :, ::-1])
plt.show()



# 使用不同的卷积核
# 创建kernel结构:
kernel = np.matrix(
    [ # 一个带有三个子列表的列表
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    np.uint8
)

"""
"""
# 图像腐蚀和膨胀
fushi_img = cv.erode(img, kernel)  # 腐蚀
# plt.figure(2)
plt.imshow(fushi_img[:, :, ::-1])
plt.show()

pengzhang_img = cv.dilate(img, kernel)
# plt.figure(3)
plt.imshow(pengzhang_img[:, :, ::-1])
plt.show()