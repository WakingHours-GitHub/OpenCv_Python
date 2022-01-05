import cv2 as cv
import numpy as np



"""


 

"""


# cap = cv.VideoCapture(file_path)
# 当然file_path你也可以指定为0, 这样默认就是打开摄像头
if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while cap.isOpened(): # 检测是否打开成功
        isread, img = cap.read()
        if isread:
            cv.imshow("img", img)

            if cv.waitKey(25)&0xff == ord('q'):
                # waitKey() 将会截取键盘上的字母，然后与FF与, 得到的结果看是否与'q'的ASCII吗相同
                break

    cap.release()
    cv.destroyAllWindows()
