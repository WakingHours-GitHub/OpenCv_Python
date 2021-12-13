import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# 直方图均衡化: -> 增强图像对比度的一种方法.
# 直方图均衡化, 一般用在曝光不足不足或者曝光过度的一些场景下
cv.equalizeHist() # 均衡化直方图。













# 自适应的直方图均衡化
# -> 分块, 然后对每一小块进行直方图均衡化.
# 显然, 如何取得的一小块是噪声点的话, 显然噪声将会被放大.
# 所以我们采用一个"对比度限制", 如果该像素超过设定阈值, 我们将其分布到其他的bins中
# 最后我们采用双线性插值(为了削弱每一小块的边界), 对每一小块进行拼接

# 创建自适应直方图对象
# clahe = cv.createCLAHE()
# 然后应用到我们的图像中去
# cl1_img = clahe.apply(img) # 得到均衡化后的图像









