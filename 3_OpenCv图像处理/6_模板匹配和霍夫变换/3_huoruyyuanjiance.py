import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



# 霍夫园检测

# API;
# circles = cv.HoughCircles(image, method, dp, minDist, param1=100, param2=100, minRadius=0,maxRadius=0 )
# image：输入图像，应输入灰度图像
# method：使用霍夫变换圆检测的算法，它的参数是CV_HOUGH_GRADIENT -> 霍夫梯度法
# dp：霍夫空间的分辨率，dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推
# minDist为圆心之间的最小距离，如果检测到的两个圆心之间距离小于该值，则认为它们是同一个圆心
# param1：边缘检测时使用Canny算子的高阈值，低阈值是高阈值的一半。
# param2：检测圆心和确定半径时所共有的阈值
# minRadius和maxRadius为所检测到的圆半径的最小值和最大值
























































