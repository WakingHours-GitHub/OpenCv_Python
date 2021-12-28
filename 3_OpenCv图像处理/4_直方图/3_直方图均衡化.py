import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 直方图均衡化: -> 增强图像对比度的一种方法.
# 直方图均衡化, 一般用在曝光不足不足或者曝光过度的一些场景下
# cv.equalizeHist() # 均衡化直方图。

# 作用:
# “直方图均衡化”是把原始图像的灰度直方图从比较集中的某个灰度区间变成在更广泛灰度范围内的分布。
# 直方图均衡化就是对图像进行非线性拉伸，重新分配图像像素值，使一定灰度范围内的像素数量大致相同。
# 这种方法提高图像整体的对比度，特别是有用数据的像素值分布比较接近时，在X光图像中使用广泛，可以提高骨架结构的显示，另外在曝光过度或不足的图像中可以更好的突出细节。

# API:
# dst = cv.equalizeHist(img)
# 参数：
#   img: 灰度图像
# 返回：
#   dst : 均衡化后的结果


# 下面来开始练习一下：
# 原图：
img = cv.imread("../../img/dog.png", 0)  # 以灰度图读入
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# 原图的hist
plt.plot(hist)
plt.show()  # 画出直方图
print(hist)

# 均衡化：
img_equalize = cv.equalizeHist(img)
plt.imshow(img_equalize, cmap=plt.cm.gray)
plt.show()

# 均衡化的hist
equalize_hist = cv.calcHist([img_equalize], [0], None, [256], [0, 256])
plt.plot(equalize_hist)
plt.show()

"""
可以看出, 均衡化后的图片对比度更高了, 但是同时也会丢失很多细节.
所以我们介绍下面一种算法:直方图均衡化.
"""

# 自适应的直方图均衡化
# -> 分块, 然后对每一小块进行直方图均衡化.
# 显然, 如何取得的一小块是噪声点的话, 显然噪声将会被放大.(因为噪点的灰度会被分散到其他地方)
# 所以我们采用一个"对比度限制", 如果该像素超过设定阈值, 我们将其分布到其他的bins中
# 最后我们采用双线性插值(为了削弱每一小块的边界), 对每一小块进行拼接

# 创建自适应直方图对象
# cv.createCLAHE(clipLimit, tileGridSize)
# clipLimit: 对比度限制，默认是40
# tileGridSize: 分块的大小，默认为8*8. (传入元组)

# 使用:
# 创建一个自适应均衡化的对象:
# clahe = cv.createCLAHE()
# 然后应用到我们的图像中去
# cl1_img = clahe.apply(img) # 得到均衡化后的图像

# 练习:
clahe = cv.createCLAHE(2.0, (8, 8))  # 第一个参数为阈值, 第二个参数为分块
img_clahe = clahe.apply(img)  # 应用到img上
img_clahe_hist = cv.calcHist([img_clahe], [0], None, [256], [0, 256])

plt.plot(img_clahe_hist)
plt.show()  # 可见, 自适应均衡化结果更好了

plt.imshow(img_clahe, cmap=plt.cm.gray)
plt.show()


# 观察不同阈值下的图像:
clahe = cv.createCLAHE(0.5, (8, 8))  # 第一个参数为阈值, 第二个参数为分块
img_clahe = clahe.apply(img)  # 应用到img上
img_clahe_hist = cv.calcHist([img_clahe], [0], None, [256], [0, 256])

plt.imshow(img_clahe, cmap=plt.cm.gray)
plt.show()