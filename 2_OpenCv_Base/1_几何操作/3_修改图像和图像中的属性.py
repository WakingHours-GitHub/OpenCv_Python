import cv2 as cv
import matplotlib.pyplot as plt

# 获取并且修改图像中的像素点：
img = cv.imread("../../img/matplot_py.png")
# 获取某个像素点的值
px = img[256, 256]
print(px)  # [255 255 255] -> 全为255 -> 说明是白色
img[256, 256] = [0, 0, 0]  # -> 直接数组复制就可以修改

# 仅仅获取一个通道的数值：
blue = img[256, 256, 0]  # -> BGR 选用0就是bule通道
print(blue)  # 0

plt.imshow(img)
plt.show()

# 获取图像的属性:
# 注意不是函数, 而是属性, 是类(对象)里面的属性
rows, cols, access = img.shape
print(f"长:{rows}, 宽:{cols}, 通道数:{access}")

print(img.size)  # 以字节为单位, 计算图形的大小

print(img.dtype)  # 获取像素值点的数据类型

# 图像的通道的拆分与合并
# b, g, r = cv.split(img) # 拆分返回三个通道
# 有时需要在B，G，R通道图像上单独工作。
# 在这种情况下，需要将BGR图像分割为单个通道。或者在其他情况下，可能需要将这些单独的通道合并到BGR图像。你可以通过以下方式完成。
B, G, R = cv.split(img)  # 图像分割
img = cv.merge((B, G, R))  # 图像通道合并
# 练习:
img_test = cv.imread("../../img/dog.png")  # read picture
b, g, r = cv.split(img_test)
# 我们将分割出来的通道单个显示
plt.imshow(b, cmap=plt.cm.gray)
plt.show()
plt.imshow(g, cmap=plt.cm.gray)
plt.show()
plt.imshow(r, cmap=plt.cm.gray)
plt.show()

# 然后我们显示原来的图片;
plt.ion()
plt.imshow(img_test[:, :, : :-1])
plt.show()
# 然后我们merge原来的图片
img_test = cv.merge((b,g,r))
plt.imshow(img_test[:, :, : :-1])
plt.show()

# 色彩空间的改变
# cv.cvtColor(src, code, dst=None, dstCn=None)
# @param src输入图像:8-bit unsigned, 16-bit unsigned (CV_16UC…) ,或者单精度浮点。
# @param code颜色空间转换代码(参见# colorconverversioncodes)。
#   cv.COLOR_BGR2GRAY : BGR↔Gray
#   cv.COLOR_BGR2HSV  : BGR→HSV
# @param DST输出图像的大小和深度与src相同。
# @param dstCn目标图像中的通道数量; 如果参数为0，则通道自动从SRC和代码中派生。

# 练习:
img = cv.imread("../../img/dog.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)
plt.imshow(img_gray)
plt.show()






"""
总结:
# IO操作:
cv.imread()
cv.imshow()
cv.imwrite()

# 在图像上绘制
cv.line()
cv.circle()
cv.rectangle()
cv.putText()

# 图像的属性:
img.shape
img.dtype
img/size

# 拆分和合并
cv.split()
cv.merge()

# 色彩空间的转换:
cv.cvtColor()
有150多种色彩转换方式, 但是我们最常用的就是BGR<->GRAY,和 BGR->HSV 
"""
























