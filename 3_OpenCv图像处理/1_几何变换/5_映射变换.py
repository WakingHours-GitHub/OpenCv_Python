import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 仿射变换 -> 平面内的变换, 所以点直接是二维的即可
# 图像的仿射变换涉及到图像的形状位置角度的变化，是深度学习预处理中常到的功能
# 仿射变换主要是对图像的缩放，旋转，翻转和平移等操作的组合。
# 步骤:
# 先指定三个点的坐标变换, 然后调用getAffineTransform获取变换矩阵
# 得到的M = [A B] 其中: A是线性变换矩阵, B是平移项
# 然后我们再用warpAffine()对矩阵进行变换

# 练习:
img = cv.imread("../../img/dog.png")
r, c = img.shape[0:2]

pts1 = np.float32(
    [
        [50, 100], [150, 150], [200, 200]
    ]

)
pts2 = np.float32(
    [
        [70, 150], [170, 170], [250, 250]
    ]
)

M = cv.getAffineTransform(pts1, pts2)
print(M)

mul = 2
res = cv.warpAffine(img, M, (mul*r, mul*c))
plt.imshow(res[:,:,::-1])
plt.show()
