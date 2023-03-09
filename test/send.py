import socket
import threading
import time
import cv2
import imagezmq
import traceback
import simplejpeg
import queue
from resource.Picture_link_method import Stitcher


capture=cv2.VideoCapture(0) # 获取摄像头视频
# capture = cv2.VideoCapture(r"D:\project\dataset\video\测试.mp4")
# 192.168.100.104 为发送端主机ip地址
sender = imagezmq.ImageSender(connect_to='tcp://192.168.137.37:5555', REQ_REP=False)
rpi_name = socket.gethostname()  # 获取主机名
time.sleep(2.0)
jpeg_quality = 95  # 调整图片压缩质量，95%
save_out = "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\result.png"
q = queue.Queue(1) #建立线程通讯队列
ref, frame = capture.read(0)
imageA = frame
imageB = frame

def createTimer():
    t = threading.Timer(1, repeat)
    t.start()


def repeat():
    # cv2.imwrite(save_out,image)
    stitcher = Stitcher()
    # (imageB, imageA) = images
    (kpsA, featuresA) = stitcher.detectAndDescribe(imageA)
    (kpsB, featuresB) = stitcher.detectAndDescribe(imageB)
    M = stitcher.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio = 0.75, reprojThresh = 4.0, method=1)
    # (matches, H, status) = M
    # result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
    # result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
    # vis = stitcher.drawMatches(imageA, imageB, kpsA, kpsB, matches, status)
    # cv2.imwrite(save_out,vis)
    print('Now:', time.strftime('%H:%M:%S', time.localtime()))
    q.put(M,kpsB,kpsA, True, None)
    createTimer()
createTimer()
time.sleep(2)
while (True):
    if q.full():
        (M,kpsB,kpsA) = q.get(True,True)
        (matches, H, status) = M
    try:
        ref, frame = capture.read(0)
        imageA = frame
        imageB = frame
        time.sleep(1 / 60)
        stitcher = Stitcher()
        result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
        # 将图片B传入result图片最左端
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
        # 生成匹配图片
        vis = stitcher.drawMatches(imageA, imageB, kpsA, kpsB, matches, status)
        result = cv2.resize(frame, (1280, 720))
        curtime = time.time()
        msg = rpi_name + '*' + str(curtime)
        # 通过simplejpeg函数将图片编码为jpeg格式，提高传输效率
        jpg_buffer = simplejpeg.encode_jpeg(result, quality=jpeg_quality,
                                            colorspace='BGR')
        cv2.imshow("test",result)
        sender.send_jpg(msg, jpg_buffer)
        cv2.imshow(rpi_name, result)
        cv2.waitKey(1)
    except:
        print(traceback.print_exc())
        break