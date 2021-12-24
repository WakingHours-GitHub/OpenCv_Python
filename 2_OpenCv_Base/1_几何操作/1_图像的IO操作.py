import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# imread(filename, flags=None)
# filename: 路径名称， flaga: 以什么方式去读取
# cv.IMREAD*COLOR：以彩色模式加载图像，任何图像的透明度都将被忽略。这是默认参数。
# cv.IMREAD*GRAYSCALE：以灰度模式加载图像
# cv.IMREAD_UNCHANGED：包括a pha通道的加载图像模式。
# 可以使用1、0或者-1来替代上面三个标志
# 注意：如果加载的路径有错误，不会报错，会返回一个None值, 所以一般在下次使用这个img(返回值)的时候才会报错

img = cv.imread("../../img/space_boat.jpg")  # 、
img_gray = cv.imread("../../img/matplot_py.png", cv.IMREAD_GRAYSCALE)

# print(img)

# 2. 显示图像:

# imshow(winname, mat)
# winname: 显示窗口的名字 需要字符串类型
# mat: 需要显示的图像
# 注意, 在调用imshow的API后, 要调用cv.waitkey()给图像绘制留下时间,否则窗口会出现无响应的情况.并且图像无法显示出来
# cv.waitKey(0) # 等待键盘输入
# cv.destroyAllWindows() # 关闭所有已打开的窗口

# 2.1 OpenCv
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()  # 关闭窗口, 并且取消分配任何相关的内存使用

arr = list(range(10))
# 回想列表的切片操作.
# img[:,::-1,:] 水平翻转
# img[::-1,:,:] 上下翻转
# img[:, :, :: -1] BGR -> RGB 通道转换 # 是根据内部的这个数组,整个翻转过来


# print(img[:,:,:])

# 2.2 matplotlib方式显示图像.
# plt.imshow() # 函数
# img[:, :, : : -1] 翻转通道.

plt.ion()  # 交互模式
plt.ioff()  # 阻塞模式
plt.imshow(img[:, :, ::-1])  # plt显示直接在右边显示
# plt.show()
# plt.show()  # display all open figures
# 为什么这里要有一个plt.show  -> 因为默认情况下figure是阻塞模式,必须要用plt.show()才能展示

# 灰度读入
img_gray = cv.imread("../../img/space_boat.jpg", cv.IMREAD_GRAYSCALE)  # 以灰度读入
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# 3. 图像保存
# imwrite(filename, img, params=None)
# filename: 保存的路径以及文件名
# img: 需要保存的图像
# params: 保存的参数吧
cv.imwrite("../image/910.png", img)  # cv.imwrites
