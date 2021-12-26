# 图像的混合
# 就是在图像相加的基础上, 增加了权重, 同理, 这两张图片也是大小相同的
# 这其实也是加法，但是不同的是两幅图像的权重不同，这就会给人一种混合或者透明的感觉。
# 图像混合的计算公式如下：
# g(x) = (1−α)f0(x) + αf1(x)

# cv.addWeighted(rain, 0.6, view, 0.4, 0)
# dst = α⋅img1 + β⋅img2 + γ
# 这里西格玛取0

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as py

rain = cv.imread("../../img/rain.jpg")
view = cv.imread("../../img/view.jpg")

img = cv.addWeighted(rain, 0.6, view, 0.4, 0)

plt.imshow(img[:,:,::-1])
plt.show()










