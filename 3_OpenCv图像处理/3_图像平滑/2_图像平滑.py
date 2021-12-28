import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 图像平滑从信号处理的角度看就是去除其中的高频信息，保留低频信息。因此我们可以对图像实施低通滤波。低通滤波可以去除图像中的噪声，对图像进行平滑。
# 根据滤波器的不同可分为均值滤波，高斯滤波，中值滤波， 双边滤波。


# 均值滤波：-> 由一个卷积框对像素进行操作.
# 优点: 计算简单, 速度快
# 缺点: 因为是平均, 所整体上看着模糊了
# cv.blur(src, ksize, anchor, borderType)
# src：输入图像
# ksize：卷积核的大小
# anchor：默认值 (-1,-1) ，表示核中心
# borderType：边界类型

# 练习:
dogsp = cv.imread("image/dogsp.jpeg")  # load picture

dog_blur = cv.blur(dogsp, (5, 5), dst=None, anchor=(-1, -1))
plt.imshow(dog_blur[:, :, ::-1])
plt.show()

# 对于高斯dog:
dog_gauss = cv.imread("image/dogGauss.jpeg")
dog_gauss_blur = cv.blur(dog_gauss, (3, 3))
plt.imshow(dog_gauss_blur[:, :, ::-1])
plt.show()

# 高斯滤波:
# 二维高斯是构建高斯滤波器的基础，其概率分布函数如下所示：
# 那么σ越大说明,标准差越大, 说明越扁平 -> 中心点对于其他邻域的权重就小
# 反之: σ越小, 说明标准差越大, 则越突起 -> 中心点对于邻域的权重就大
# 在x,y方向上都是正态分布。
# 在图像平滑中, 我们只需要将中心作为原点, 然后按照曲线上的位置分配权重, 就可以得到一个加权平均值.

"""
高斯平滑的流程：
假定中心点的坐标是（0,0），那么距离它最近的8个点的坐标如下：
为了计算权重矩阵，需要设定σ的值。假定σ=1.5，则模糊半径为1的权重矩阵如下
这9个点的权重总和等于0.4787147，如果只计算这9个点的加权平均，还必须让它们的权重之和等于1，因此上面9个值还要分别除以0.4787147，得到最终的权重矩阵。-> 归一化

对所有点重复这个过程，就得到了高斯模糊后的图像。如果原图是彩色图片，可以对RGB三个通道分别做高斯平滑。
"""
# API:
# cv2.GaussianBlur(src,ksize,sigmaX,sigmay,borderType)
# src: 输入图像
# ksize:高斯卷积核的大小，注意：卷积核的宽度和高度都应为奇数，且可以不同 -> 权重矩阵的大小
# sigmaX: 水平方向的标准差  -> 标准差
# sigmaY: 垂直方向的标准差，默认值为0，表示与sigmaX相同
# borderType:填充边界类型

# 练习：直接对dog_gauss
dog_gauss_blur = cv.GaussianBlur(dog_gauss, (3, 3), 2)
plt.imshow(dog_gauss_blur[:, :, ::-1])
plt.show()

# 中值滤波
# 中值滤波是一种典型的非线性滤波技术，基本思想是用像素点邻域灰度值的中值来代替该像素点的灰度值。
# 取的是中值, 所以对极值点有抑制作用, 所以对椒盐噪声效果很好
# 中值滤波对椒盐噪声（salt-and-pepper noise）来说尤其有用，因为它不依赖于邻域内那些与典型值差别很大的值。

# cv.medianBlur(src, ksize)
# src：输入图像
# ksize：卷积核的大小 -> 必须是方阵

# 练习:
dog_blur = cv.medianBlur(dogsp, 3)
plt.imshow(dog_blur[:, :, ::-1])
plt.show()
