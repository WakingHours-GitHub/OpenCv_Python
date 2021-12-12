# as 导入模块起别名
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 画直线：
# cv.line(img, start, end, color, thickness, lineType, shift)
# img:要绘制直线的图像
# Start,end: 直线的起点和终点(传入一个元组, 代表坐标) -> (x, y)
# color: 线条的颜色
# Thickness: 线条宽度
# lineType: 线的类型

# 画一个园
# cv.circle(img, center, radius, color, thickness, lineType, shift)
# img:要绘制圆形的图像
# Center, radius: 圆心和半径 -> 圆心为元组(x, y), radius单位为像素
# color: 线条的颜色
# Thickness: 线条宽度，为-1时生成闭合图案并填充颜色

# 画一个矩形
# cv.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# img:要绘制矩形的图像
# pt1, pt2: 矩形的左上角和右下角坐标 -> 同样都是一个元组, 代表坐标
# color: 线条的颜色
# Thickness: 线条宽度

# 添加文字：
# cv.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
# img: 图像
# text：要写入的文本数据
# org：文本的放置位置
# fontFace：字体
# fontScale :字体大小


# 练习:
img = np.zeros((512, 512, 3), np.uint8)  # 以uint8数据类型创建一个512*512*3的矩阵, 实际上就是img(看你用什么方式去看它)
# uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0–255。这里要注意如何转化到uint8类型。
# print(img)
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.circle(img, (256, 256), 128, (0, 0, 255), 4, 4)
cv.line(img, (256, 256), (511, 0), (0, 255, 0), 6)
cv.rectangle(img, (0, 256), (256, 511), (255, 255, 255), 5)

cv.putText(img, "HEL", (256, 256), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=5, color=(255, 255, 255), thickness=5)

cv.imwrite("../../img/matplot_py.png", img)

plt.imshow(img)
plt.show()

# 真正的艺术:
plt.figure(1)
realArt = np.zeros((512, 512, 3), np.uint8)  #
