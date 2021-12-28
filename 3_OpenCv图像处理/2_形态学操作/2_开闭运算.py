import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 开闭运算:
# 开运算和闭运算是将腐蚀和膨胀按照一定的次序进行处理。
# 但这两者并不是可逆的，即先开后闭并不能得到原来的图像。

# 开运算:
# 开运算是先腐蚀后膨胀
# 其作用是：分离物体，消除小区域。
# 特点：消除噪点，去除小的干扰块，而不影响原来的图像。

# 闭运算:
# 闭运算与开运算相反，是先膨胀后腐蚀
# 作用是消除“闭合”物体里面的孔洞
# 特点：可以填充闭合区域。

# API
# cv.morphologyEx(img, op, kernel)
# img: 要处理的图像
# op: 处理方式：若进行开运算，则设为cv.MORPH_OPEN，若进行闭运算，则设为cv.MORPH_CLOSE
# Kernel： 核结构


# 练习:
letterOpen = cv.imread("letteropen.png")  # -> 有很多的噪点, 所以我们应该先腐蚀, 然后在膨胀, 所以是开环操作
plt.imshow(letterOpen[:, :, ::-1])
plt.show()

kernel = np.ones((10, 10), np.uint8)  # 创建核
img_open = cv.morphologyEx(letterOpen, cv.MORPH_OPEN, kernel)
plt.imshow(img_open[:, :, ::-1])  # 可见, 很好的消除了噪点
plt.show()

# 闭环操作
letterClose = cv.imread("letterclose.png")  # 我们可以看到这张图片有很多空洞,
# 于是我们使用先膨胀,后腐蚀的 -> 对应闭环运算
plt.imshow(letterClose[:, :, ::-1])
plt.show()


img_close = cv.morphologyEx(letterClose, cv.MORPH_CLOSE, kernel)
plt.imshow(img_close[:, :, ::-1])
plt.show()
# 效果不太好,我们使用别的core试试

kernel = np.ones((12,12), np.uint8)

img_close = cv.morphologyEx(letterClose, cv.MORPH_CLOSE, kernel)
plt.imshow(img_close[:, :, ::-1])
plt.show()