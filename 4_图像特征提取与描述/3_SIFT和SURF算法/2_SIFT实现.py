import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# sift算法的实现
# 1. 实例化sift
# sift = cv.xfeatures2d.SIFT_create() (旧的, 新版本已经不这样用了)
# 返回一个sift检测对象
# 2. 利用sift对象进行detect(检测)
# kp,des = sift.detectAndCompute(gray,None)
# 参数：
#   gray: 进行关键点检测的图像，注意是灰度图像
# 返回：
#   kp: 关键点信息，包括位置，尺度，方向信息
#   des: 关键点描述符，每个关键点对应128个梯度信息的特征向量
# 3. 然后将关键点检测结果绘制在图像上
# cv.drawKeypoints(image, keypoints, outputimage, color, flags)
# image: 原始图像
# keypoints：关键点信息，将其绘制在图像上
# outputimage：输出图片，可以是原始图像
# color：颜色设置，通过修改（b,g,r）的值,更改画笔的颜色，b=蓝色，g=绿色，r=红色。
# flags：绘图功能的标识设置
#   cv2.DRAW_MATCHES_FLAGS_DEFAULT：创建输出图像矩阵，使用现存的输出图像绘制匹配对和特征点，对每一个关键点只绘制中间点
#   cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG：不创建输出图像矩阵，而是在输出图像上绘制匹配对
#   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS：对每一个特征点绘制带大小和方向的关键点图形
#   cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS：单点的特征点不被绘制

# 新的版本: OpenCv4.0以上的
# 1. 实例化sift对象
# sift = cv.SIFT_create() # 实例化sift对象
# 2. 返回关键点信息:
# kp = sift.detect(gray, None) # 检测关键关键点信息
# 参数：
#   gray: 进行关键点检测的图像，注意是灰度图像
# 返回：
#   kp: 关键点信息，包括位置，尺度，方向信息
#   des: 关键点描述符，每个关键点对应128个梯度信息的特征向量
# kp, des = sift.detectAndCompute

# cv.drawKeypoints() # 画出描述点

# dog = cv.imread("../../img/dog.png")
tv = cv.imread("tv.jpg")
tv_gray = cv.cvtColor(tv, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(tv_gray, None)
cv.drawKeypoints(tv, kp, tv, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(tv[:, :, ::-1])
plt.show()


# 测试
if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    sift = cv.SIFT_create()
    while True:
        is_open, img = cap.read()
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kp,des = sift.detectAndCompute(img_gray, None) # 返回特征点
        cv.drawKeypoints(img, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # 画图

        cv.imshow("img", img)
        cv.waitKey(1)

