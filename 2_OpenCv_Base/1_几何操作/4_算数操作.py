import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# plt.ion() # 后面需要配合pause

# 你可以使用OpenCV的cv.add()函数把两幅图像相加，或者可以简单地通过numpy操作添加两个图像
# 如res = img1 + img2。两个图像应该具有相同的大小和类型，或者第二个图像可以是标量值。
# 但是cv.add()和numpy的直接相加有不同
# cv.add是饱和操作, 而numpy的相加是取模操作
pic = cv.imread("../../img/view.jpg")
rain = cv.imread("../../img/rain.jpg")

# cv.add:
cv_add = cv.add(pic, rain)
plt.imshow(cv_add[:,:,::-1])
plt.show()

# numpy_add:
numpy_add = pic + rain
plt.imshow(numpy_add[:,:,::-1])
plt.show()













































