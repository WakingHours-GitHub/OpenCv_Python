import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 基于搜索算法:

# subel算子：_> 效率高, 简单, 但是检测效果不理想
# 分别对x方向和y防线获取x, y的Sobel算子
# cv.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
# src：传入的图像
# ddepth: 图像的深度, 图像深度是指像素深度中实际用于存储图像的灰度或色彩所需要的比特位数, 我们的图像都是uint8的,
#   但是会发生截断, 所以我们使用CV_16S, 然后再转换回去
# dx和dy: 指求导的阶数，0表示这个方向上没有求导，取值为0、1。
# ksize: 是Sobel算子的大小，即卷积核的大小，必须为奇数1、3、5、7，默认为3。
#   注意：如果ksize=-1，就演变成为3x3的Scharr算子
#   Scharr算子: 只能是3*3的卷积核, 但是比Sobel更精准
# scale：缩放导数的比例常数，默认情况为没有伸缩系数。
# borderType：图像边界的模式，默认值为cv2.BORDER_DEFAULT。

# Sobel函数求完导数后会有负值，还有会大于255的值。而原图像是uint8，即8位无符号数，所以Sobel建立的图像位数不够，会有截断。
# 因此要使用16位有符号的数据类型，即cv2.CV_16S。(16位浮点型)处理完图像后，
# 再使用cv2.convertScaleAbs()函数将其转回原来的uint8格式，否则图像无法显示。
# API:
# cv.convertScaleAbs()

# Sobel算子是在两个方向计算的，最后还需要用cv2.addWeighted( )函数将其组合起来
# 然后我们需要混合：
# 加权混合 -> 前面的函数
# cv.addWeighted()

# 练习:
img = cv.imread("../../img/dog.png", 0) # load gray picture
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# 分别对x,y方向求导
x = cv.Sobel(img, cv.CV_16S, 1, 0)
y = cv.Sobel(img, cv.CV_16S, 0, 1)
# 转换:
uint8_x = cv.convertScaleAbs(x)
uint8_y = cv.convertScaleAbs(y)

plt.imshow(uint8_x, cmap=plt.cm.gray)
plt.show() # 对x求导只有竖的线条


img_edge = cv.addWeighted(uint8_x, 0.5, uint8_y, 0.5, 0)
plt.imshow(img_edge, cmap=plt.cm.gray)
plt.show()








# scharr算子
# cv.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
# 当ksize = -1的时候, 就是利用Schaar算子进行边缘检测
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)

uint8_x = cv.convertScaleAbs(x)
uint8_y = cv.convertScaleAbs(y)

img_edge = cv.addWeighted(uint8_x, 0.5, uint8_y, 0.5, 0)
plt.imshow(img_edge, cmap=plt.cm.gray)
plt.show()


#
if __name__ == '__main__':
    # 开始调用摄像头
    cap = cv.VideoCapture(0)
    while True:
        isread, img = cap.read()
        if isread == True:
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            img_gray_sobel_x = cv.Sobel(img_gray, cv.CV_16S, 1, 0, -1)
            img_gray_sobel_y = cv.Sobel(img_gray, cv.CV_16S, 0, 1, -1)

            abs_x = cv.convertScaleAbs(img_gray_sobel_x)
            abs_y = cv.convertScaleAbs(img_gray_sobel_y)

            result = cv.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

            cv.imshow("result", result)
            cv.waitKey(1)







            cv.imshow("img", img)
            cv.waitKey(1)




