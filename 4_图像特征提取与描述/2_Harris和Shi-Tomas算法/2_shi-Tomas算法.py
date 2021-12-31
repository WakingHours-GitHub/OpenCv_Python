import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# shi-Tomas 角点检测算法.
# R = min(l1, l2)

# API:
# corners = cv2.goodFeaturesToTrack ( image, maxcorners, qualityLevel, minDistance )
# Image: 输入灰度图像
# maxCorners : 获取角点数的数目。需要绘制的角点的数目
# qualityLevel：该参数指出最低可接受的角点质量水平，在0-1之间。越大, 说明筛选点质量越高, 点越少
# minDistance：角点之间最小的欧式距离，避免得到相邻特征点。小于这个距离的都当成一个点, 选取质量最好的那个点

# 返回值:
# Corners: 搜索到的角点，在这里所有低于质量水平的角点被排除掉，然后把合格的角点按质量排序
# 然后将质量较好的角点附近（小于最小欧式距离）的角点删掉，最后找到maxCorners个角点返回。



tv = cv.imread("tv.jpg")
tv_gray = cv.cvtColor(tv, cv.COLOR_BGR2GRAY)
tv_gray_float32 = np.float32(tv_gray)

circles = cv.goodFeaturesToTrack(tv_gray_float32, 1000, 0.01, 20)
# 返回得到的就是circles, 检查角点坐标(x, y)




for circle in circles:
    x, y = np.int32(circle.ravel())
    # 注意, 这里要将x, y转换回int类型的数值

    print(circle.ravel())
    cv.circle(tv, (x, y), 2, (0, 0, 255), -1)

plt.imshow(tv[:, :, ::-1])
plt.show()
