import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 直方图是反应图像中像素强度分布的图形的表达方式
# 他统计了每个强度所具有的像素个数
# 不同的图像的直方图可能是相同的
# 直方图的一些术语和细节：
#
# dims：需要统计的特征数目。在上例中，dims = 1 ，因为仅仅统计了灰度值。
# bins：每个特征空间子区段的数目，可译为 “直条” 或 “组距”，在上例中， bins = 16。
# range：要统计特征的取值范围。在上例中，range = [0, 255]。
# 直方图的意义：
#
# 直方图是图像中像素强度分布的图形表达方式。
# 它统计了每一个强度值所具有的像素个数。
# 不同的图像的直方图可能是相同的

# API:
# cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
# images: 原图像。当传入函数时应该用中括号 [] 括起来，例如：[img]。
# channels: 如果输入图像是灰度图，它的值就是 [0]；如果是彩色图像的话，传入的参数可以是 [0]，[1]，[2] 它们分别对应着通道 B，G，R。 　　
# mask: 掩模图像。要统计整幅图像的直方图就把它设为 None。但是如果你想统计图像某一部分的直方图的话，你就需要制作一个掩模图像，并使用它。（后边有例子） 　　
# histSize:BIN 的数目。也应该用中括号括起来，例如：[256]。 　　
# ranges: 像素值范围，通常为 [0，256]

# 在使用calcHist的时候, 我们传入参数时, 都必须加入[] 这是由底层所决定的

# 练习:
img = cv.imread("../../img/space_boat.jpg", 0) # 读入灰度图
space_boat_hsh = cv.calcHist([img], [0], None, [256], [0, 256])

plt.figure(1, figsize=(16, 9), dpi=150)
# fig = plt.figure(figsize=(a, b), dpi=dpi)
# 其中：
# figsize 设置图形的大小，a 为图形的宽， b 为图形的高，单位为英寸
# dpi 为设置图形每英寸的点数
# 则此时图形的像素为：
# px, py = a*dpi, b*dpi # pixels


plt.plot(space_boat_hsh)
plt.show()


































