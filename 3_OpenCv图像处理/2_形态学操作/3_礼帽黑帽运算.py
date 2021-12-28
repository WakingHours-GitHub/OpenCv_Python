import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# 礼帽和黑帽运算



# 礼帽运算: -> 拿到图像周围比较亮的区域
# 原图像与“开运算“的结果图之差，如下式计算：
# dist = src - open(src, kernel)
#因为开运算带来的结果是放大了裂缝或者局部低亮度的区域，因此，从原图中减去开运算后的图，得到的效果图突出了比原图轮廓周围的区域更明亮的区域，且这一操作和选择的核的大小相关。
# 礼帽运算用来分离比邻近点亮一些的斑块。当一幅图像具有大幅的背景的时候，而微小物品比较有规律的情况下，可以使用顶帽运算进行背景提取。


# 黑帽运算 -> 拿到图像周围比较暗的区域
# 为”闭运算“的结果图与原图像之差。数学表达式为：
# dist = close(src, kernel) - src
# 黑帽运算后的效果图突出了比原图轮廓周围的区域更暗的区域，且这一操作和选择的核的大小相关。
# 黑帽运算用来分离比邻近点暗一些的斑块。

# API:
# cv.morphologyEx(img, op, kernel)
# img: 要处理的图像
# op: 处理方式：
#   cv.MORPH_CLOSE          闭运算
#   cv.MORPH_OPEN           开运算
#   cv.MORPH_TOPHAT         礼帽运算
#   cv.MORPH_BLACKHAT       黑帽运算
# Kernel： 核结构

# 练习:
letter_open = cv.imread("letteropen.png")
kernel = np.ones((10,10), np.uint8)

# 进行礼帽运算
img_tophat = cv.morphologyEx(letter_open, cv.MORPH_TOPHAT, kernel)
plt.imshow(img_tophat[:,:,::-1])
plt.show()

# 进行黑帽运算
letter_close = cv.imread("letteropen.png")
img_blackhat = cv.morphologyEx(letter_close, cv.MORPH_BLACKHAT, kernel)
plt.imshow(img_blackhat[:,:,::-1])
plt.show()























