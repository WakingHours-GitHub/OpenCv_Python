


"""
在OpenCV中我们要获取一个视频，需要创建一个VideoCapture对象，指定你要读取的视频文件：
1. 创建读取视频的对象
    cap = cv.VideoCapture(filepath)
        参数:
            filepath: 视频文件路径
        返回:
            返回一个capture对象
2. 视频的属性信息
    2.1. 获取视频的某些属性
        retval = cap.get(propId)
            pripId: 从0~18的数字, 每个数字表示视频的属性
            索引:     flags                  意义
            0       cv2.CAP_PROP            视频文件当前的位置(ms)
 

"""

import cv2 as cv

# cap = cv.VideoCapture(file_path)
# 当然file_path你也可以指定为0, 这样默认就是打开摄像头
if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while cap.isOpened(): # 检测是否打开成功
        isread, img = cap.read()
        if isread:
            cv.imshow("img", img) # 显示.

            if cv.waitKey(25)&0xff == ord('q'):
                # waitKey() 将会截取键盘上的字母，然后与FF与, 得到的结果看是否与'q'的ASCII吗相同
                break

    cap.release() # 释放资源
    cv.destroyAllWindows() # 销毁所有的窗口
