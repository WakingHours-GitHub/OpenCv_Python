import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# subel算子：
# 分别对x方向和y防线获取x, y的Sobel算子
# cv。Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)

# 然后我们需要进行格式的转换
# cv.convertScaleAbs()



# 然后我们需要混合：
# 加权混合 -> 前面的函数
# cv.addWeighted()






# scharr算子
# cv。Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
# 当ksize = -1的时候, 就是利用Schaar算子进行边缘检测





