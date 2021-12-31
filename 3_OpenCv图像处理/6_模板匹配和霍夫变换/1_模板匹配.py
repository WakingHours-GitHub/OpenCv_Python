import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 模板匹配：
# 所谓的模板匹配，就是在给定的图片中查找和模板最相似的区域，该算法的输入包括模板和图片
# 整个任务的思路就是按照滑窗的思路不断的移动模板图片，计算其与图像中对应区域的匹配度，最终将匹配度最高的区域选择为最终的结果。

# 对于每一个位置将计算的相似结果保存在结果矩阵（R）中。如果输入图像的大小（WxH）且模板图像的大小(wxh)，则输出矩阵R的大小为（W-w + 1,H-h + 1）将R显示为图像，如下图所示：
# res = cv.matchTemplate(img,template,method) # 返回的就是R矩阵
# img: 要进行模板匹配的图像
# Template ：模板
# method：实现模板匹配的算法，主要有：
#   平方差匹配(CV_TM_SQDIFF)：利用模板与图像之间的平方差进行匹配，最好的匹配是0，匹配越差，匹配的值越大。
#   相关匹配(CV_TM_CCORR)：利用模板与图像间的乘法进行匹配，数值越大表示匹配程度较高，越小表示匹配效果差。
#   利用相关系数匹配(CV_TM_CCOEFF)：利用模板与图像间的相关系数匹配，1表示完美的匹配，-1表示最差的匹配。
# 完成匹配后，使用cv.minMaxLoc()方法查找最大值所在的位置即可。如果使用平方差作为比较方法，则最小值位置是最佳匹配位置。

"""
注意：新的OpenCv中, method的方法, 前面均不带CV了
    即:
        TM_SQDIFF -> 平方差算法, 数值越是小, 匹配度则越高
        TM_CCORR  -> 相关匹配算法, 
        TM_CCOEFF -> 相关系数算法
        


"""

src_img = cv.imread("wulin.jpeg")  # 原始图像
sub_img = cv.imread("bai.jpeg")
plt.imshow(sub_img[:,:,::-1])
plt.show()

h, w = sub_img.shape[0:2]  # 返沪高度和宽度
# y, x  方向, 分别是高,宽
print(h, w)
res = cv.matchTemplate(src_img, sub_img, method=cv.TM_CCORR)

minVal, maxVak, minLoc, maxLoc = cv.minMaxLoc(res)
tob_left = maxLoc # 最大值的位置坐标（左上角）
down_right = (maxLoc[0] + w, maxLoc[-1] + h) # 获取右下角的坐标
# -> 表示x
# |
# v 表示y
cv.rectangle(src_img, tob_left, down_right, (0, 255, 0), 2)

plt.imshow(src_img[:, :, ::-1])
plt.show()
