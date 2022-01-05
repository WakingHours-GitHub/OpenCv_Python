import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Canny边缘检测算法 -> 被认为是最优的边缘检测算法
# 原理:
# 第一步: 噪声去除
# cv.blur() # 均值滤波
# cv.GaussianBlur() # 高斯滤波
# cv.medianBlur() # 中值滤波

# 第二步: 计算图像梯度
# 使用Sobel算子计算水平方向和竖直方向的一阶导数(Gx和Gy)
#

# 第三步非极大值抑制
# 在获得梯度的方向和大小之后，对整幅图像进行扫描，去除那些非边界上的点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯度方向的点中最大的。
# cv.Sobel(src, deepeth, dx, dy, ksize)

# 第四步: 滞后阈值
# 现在要确定真正的边界。
# 我们设置两个阈值： minVal 和 maxVal。-> 这是非常关键的
# 当图像的灰度梯度高于 maxVal 时被认为是真的边界(认为是边界), 低于 minVal 的边界会被抛弃。
# -> 所以minVal决定了哪些保留, 哪些不保留, 只有与边缘点相连接的才认为是边缘
# -> 而maxVal决定了那个是边界

# 如果介于两者之间的话, 就要看这个点是否与某个被确定为真正的边界点相连，
# 如果是就认为它也是边界点, 如果不是就抛弃。如下图：

# API：
# canny = cv2.Canny(image, threshold1, threshold2)
# image:灰度图，
# threshold1: minval，较小的阈值将间断的边缘连接起来
# minval小, 说明
# threshold2: maxval，较大的阈值检测图像中明显的边缘

# 使用实例：
horse = cv.imread("horse.jpg", 0)  # 以灰度图读入

# 设置Canny阈值
low = 200
high = 300

canny_img = cv.Canny(horse, low, high)  # 返回Canny边缘检测后的图像

plt.imshow(canny_img, cmap=plt.cm.gray)  # 以灰度图展示
plt.show()

# 练习: 练习宇宙飞船的特征点提取
boat = cv.imread("../../img/space_boat.jpg", cv.IMREAD_GRAYSCALE)  # 以灰度方式读入

minVar = 50
maxVar = 500
# 进行Canny边缘检测:
canny_boat = cv.Canny(boat, minVar, maxVar)  # 返回边缘检测的图形.

plt.imshow(canny_boat, cmap=plt.cm.gray)
plt.show()


def Canny_gray():
    cap = cv.VideoCapture(0)

    while True:
        is_open, img = cap.read()
        if is_open:
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            img_gray_blur = cv.medianBlur(img_gray, 3)
            # 注意, gauss的ksize是元组, 所以要传入(x, y)
            img_gray_gauss_blur = cv.GaussianBlur(img_gray_blur, (3, 3), 2)
            img_canny = cv.Canny(img_gray_gauss_blur, 40, 70)

            cv.imshow("img_canny", img_canny)
            cv.imshow("img_gray", img_gray)
            cv.imshow("img", img)
            cv.waitKey(1)
            # cv.destroyAllWindows()


def Canny_BGR():
    cap = cv.VideoCapture(0)
    while True:
        is_open, img = cap.read()
        if is_open:
            b, g, r = cv.split(img)
            minVar = 40
            maxVar = 60
            b_canny = cv.Canny(b, minVar, maxVar)
            g_canny = cv.Canny(g, minVar, maxVar)
            r_canny = cv.Canny(r, minVar, maxVar)

            img_canny = cv.merge((b_canny, g_canny, r_canny))
            img_canny_gauss_blur = cv.GaussianBlur(img, (3, 3), 1.5)

            cv.imshow("img_canny_gauss_blur", img_canny_gauss_blur)
            cv.imshow("img_canny", img_canny)
            cv.imshow("img", img)
            cv.waitKey(1)


# 练习：
if __name__ == '__main__':
    # Canny_BGR()
    Canny_gray()
