import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 掩膜就是提取我们感兴趣的区域的 !!!
# 掩膜是一个二值图像:
# 1代表高亮区域, 代表要处理的区域
# 0代表黑色区域, 代表要屏蔽的区域


# 掩膜的主要用途是：
#
# 提取感兴趣区域：用预先制作的感兴趣区掩模与待处理图像进行”与“操作，得到感兴趣区图像，感兴趣区内图像值保持不变，而区外图像值都为0。
# 屏蔽作用：用掩模对图像上某些区域作屏蔽，使其不参加处理或不参加处理参数的计算，或仅对屏蔽区作处理或统计。
# 结构特征提取：用相似性变量或图像匹配方法检测和提取图像中与掩模相似的结构特征。
# 特殊形状图像制作

# 特定区域直方图的应用
# 我们使用cv.calcHist（）来查找完整图像的直方图。 如果要查找图像某些区域的直方图，该怎么办？
# 只需在要查找直方图的区域上创建一个白色的掩膜图像，否则创建黑色， 然后将其作为掩码mask传递即可。

# 图像位操作:
# bitwise_and(src1, src2, dst=None, mask=None)
# src1、src2：为输入图像或标量，标量可以为单个数值或一个四元组
# dst：可选输出变量，如果需要使用非None则要先定义，且其大小与输入变量相同
# mask：图像掩膜，可选参数，为8位单通道的灰度图像，用于指定要更改的输出图像数组的元素，即输出图像像素只有mask对应位置元素不为0的部分才输出，否则该位置像素的所有通道分量都设置为0


# 练习:
img = cv.imread("../../img/dog.png", 0)  # load gray picture
row, col = img.shape[0:2]
dog_hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

plt.plot(dog_hist)
plt.show()

# 创建掩膜:
mask = np.zeros((row, col), np.uint8)  # 创建一个与图像大小相同的掩膜
mask[0:250, 400: 690] = 1  # 高亮, 处理的区域

mask_dog = cv.bitwise_and(img, img, mask=mask)
plt.imshow(mask_dog, cmap=plt.cm.gray)
plt.show()

# 然后对掩膜后的图像进行直方图
dog_mask_hist = cv.calcHist([img], [0], mask, [256], [0, 256])
plt.plot(dog_mask_hist)
plt.show()
