import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 缩放是对图像的大小进行调整，即使图像放大或缩小。
# resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
# src : 输入图像
# dsize: 绝对尺寸，直接指定调整后图像的大小
# fx,fy: 相对尺寸，将dsize设置为None，然后将fx和fy设置为比例因子即可

img = cv.imread("../../img/dog.png")
plt.imshow(img[:,:,::-1])
plt.show()

row, col = img.shape[0:2]
print(row, col)
# 绝对尺寸
res = cv.resize(img, (2*row, 2*col))

plt.imshow(res[:,:,::-1])
plt.show()

# 相对尺寸
res = cv.resize(img,None, fx=0.5, fy=0.6)
plt.imshow(res[:,:,::-1])
plt.show()