import cv2
import imagezmq
import traceback
import time
import simplejpeg
import threading


def createTimer():
    t = threading.Timer(2, repeat)
    t.start()


def repeat():
    print('Now:', time.strftime('%H:%M:%S', time.localtime()))
    save_out = "D:\\pythonProject\\resource\\result\\result.png"
    cv2.imwrite(save_out, image)
    createTimer()



# 接收发送端数据，输入发送端的ip地址
image_hub = imagezmq.ImageHub(open_port='tcp://192.168.137.37:5555', REQ_REP=False)
frame_count = 1
time1 = 0
createTimer()
while True:
    try:
        time1 = time.time() if frame_count == 1 else time1
        name, image = image_hub.recv_jpg()
        # 解码
        image = simplejpeg.decode_jpeg(image, colorspace='BGR')
        cv2.imshow(name.split('*')[0], image)
        cv2.waitKey(1)
        time2 = time.time()
        print(image.shape[:2], int(frame_count / (time2 - time1)))
        frame_count += 1
    except:
        print(traceback.format_exc())
        break