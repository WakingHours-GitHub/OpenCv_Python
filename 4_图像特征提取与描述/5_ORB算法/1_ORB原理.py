"""
SIFT和SURF算法是受专利保护的, 他们在使用时需要收费
但是ORB不需要, 它可以用来对图像中的关键点快速创建特征向量, 并且使用这些特征向量来识别图像中的对象

ORB算法结合了Fast算法和Brief算法, 提出了构造金字塔, 为Fast特征的点添加了方向, 从而使得关键点具有了尺度不变性和旋转不变性.
算法流程:
    构造尺度金字塔. 每层仅有一幅图像.
    在不同尺度上利用Fast算法检测特征点, 采用Harris角点响应函数, 根据角点的响应值排序, 选取前N个特征点, 作为本尺度的特征点
    计算特征点的主方向, 计算以特征为圆心半径为r的圆形领域内的灰度质心位置, 将从特征点位置到质心位置做特征点的主方向/.
    为了解决旋转不变性, 将特征点的邻域旋转到主方向上利用Brief算法构建特征描述符, 至此就得到了ORB的特征描述向量.

Brief算法: 是一种特征描述子提取算法, 并非特征点的提取算法, 一种生成二值化描述子的算法, 不提取代价低, 匹配只需要使用简单的汉明距离
    利用比特之间的异或操作就可以完成, 因此Brief算法, 时间代价低, 空间代价低, 效果比较好
步骤如下:
    1. 图像滤波
    2. 选取点对
        以特征点为中心, 取s*s的邻域窗口, 在窗口中随机选取N组点对, 一般是N=128,256,512, 默认是256
        如何选取点对: 采样
            x,y方向平均分布采样
            x,y服从Gauss()各项同样采样
            x服从一个gauss分布, y服从另一个gauss分布
            x,y从网格中随机获取
            x一直在(0, 0), y从网格中随机选取
    3. 构建描述符

API:
在OpenCv中实现ORB算法, 使用的是:
    1. 实例化ORB:
        # orb = cv.xfeatures2d.orb_create(nfeatures)
        orb = cv.ORB_create() # 实际上该函数属于是xfeature2d这个包中
        参数：
            nfeatures: 特征点的最大数量
        返回:
            返回一个orb对象
    2. 利用orb.detectAndCompute()检测关键点并且计算
        kp, des = orb.detectAndCompute(gray, None)
        参数:
            gray: 进行关键点检测的图像, 注意是灰度图像
        返回:
            kp: 关键点信息, 包括位置, 尺度, 方向信息
            des: 关键点描述符, 每个关键点Brief特征向量, 二进制字符串
    3. 将关键点检测结果绘制在图像上
        cv.drapKeypoints(image, keypoints, outputtimage, color, flags)



"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 演示一下: ORB:

img = cv.imread("tv.jpg") # load pic
# new a orb object
orb = cv.ORB_create(nfeatures=500)

kp, des = orb.detectAndCompute(img, None)
print(des.shape) # (500, 32) # 默认是8位, 也就是256


img_kp_draw = cv.drawKeypoints(img, kp, None, flags=0)
plt.imshow(img_kp_draw[:,:,::-1])
plt.show()

