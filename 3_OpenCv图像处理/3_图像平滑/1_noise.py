import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



# 图像噪声：
# 由于图像采集、处理、传输等过程不可避免的会受到噪声的污染，妨碍人们对图像理解及分析处理。常见的图像噪声有高斯噪声、椒盐噪声等。

# 椒盐噪声：
# 椒盐噪声也称为脉冲噪声，是图像中经常见到的一种噪声，它是一种随机出现的白点或者黑点，可能是亮的区域有黑色像素或是在暗的区域有白色像素（或是两者皆有）。

# 高斯噪声:
# 高斯噪声是指噪声密度函数服从高斯分布的一类噪声。所产生的颜色不只是黑白两种颜色了, 是更多的颜色



# 先读取图片数据
dogsp = cv.imread("image/dogsp.jpeg") # read picture
doggauss = cv.imread("image/dogGauss.jpeg")

# 分别对doggauss和dogsp进行处理
# 对图像进行平滑处理
# 均值滤波
# cv.blur()



# 高斯滤波
# cv.GaussianBlur()
# 中值滤波
# cv.medianBlur()





