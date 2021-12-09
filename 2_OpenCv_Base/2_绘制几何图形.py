# as 导入模块起别名
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



# cv.line(img, start, end, color, thickness)
# img: 在那张图片上绘制













# 练习:
img = np.zeros((512, 512, 3), np.uint8) # 以uint8数据类型创建一个512*512*3的矩阵, 实际上就是img(看你用什么方式去看它)
# uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0–255。这里要注意如何转化到uint8类型。
# print(img)
cv.line(img, (0, 0), (511, 511), (255,0,0), 5)
cv.circle(img, (256, 256), 128, (0,0,255), 4, 4)
cv.line(img, (256, 256), (511, 0), (0, 255, 0), 6)
cv.rectangle(img, (0, 256), (256, 511), (255, 255, 255), 5)







plt.imshow(img)
plt.show()


