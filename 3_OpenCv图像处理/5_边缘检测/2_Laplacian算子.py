import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt






# Laplacian是利用二阶导数进行边缘检测的算子
# f''(x) = f(x+1)+f(x-1)-2f(x)
# 所以使用的卷积核：
"""
kerenl = [
    0 1 0
    1 -4 1
    0 1 0
]
"""
# API：
# laplacian = cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
# Src: 需要处理的图像，
# Ddepth: 图像的深度，-1表示采用的是原图像相同的深度，目标图像的深度必须大于等于原图像的深度；
# ksize：算子的大小，即卷积核的大小，必须为1,3,5,7。


# 练习:

img = cv.imread("../../img/dog.png", 0)
img_laplacian = cv.Laplacian(img, cv.CV_16S, ksize=3)
img_laplacian_abs = cv.convertScaleAbs(img_laplacian)

plt.imshow(img_laplacian_abs, cmap=plt.cm.gray)
plt.show()









