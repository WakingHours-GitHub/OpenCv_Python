import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# 图像金字塔：
# cv.pyrUp(img)       #对图像进行上采样
# cv.pyrDown(img)        #对图像进行下采样

img = cv.imread("../../img/dog.png")
plt.imshow(img[:,:,::-1])
plt.show()

imgup = cv.pyrUp(img) # 向上采样, 变大
plt.imshow(imgup[:,:,::-1])
plt.show()

imgdown = cv.pyrDown(img) # 向下采样, 缩小
plt.imshow(imgdown[:,:,::-1])
plt.show()








