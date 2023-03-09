import os
import cv2

image = cv2.imread("D:\\pythonProject\\resource\\result\\80.jpg")
size = image.shape
w = size[1] #宽度

h = size[0] #高度

def makeVideo(path, size):
    filelist = os.listdir(path)
    filelist2 = [os.path.join(path, i) for i in filelist]
    print(filelist2)
    fps = 1  # 我设定位视频每秒1帧，可以自行修改
    # size = (1920, 1080)  # 需要转为视频的图片的尺寸，这里必须和图片尺寸一致
    video = cv2.VideoWriter(path + "\\Video.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                            size)

    for item in filelist2:
        print(item)
        if item.endswith('.jpg'):
            print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = r'D:\pythonProject\resource\result'
    # 需要转为视频的图片的尺寸,必须所有图片大小一样，不然无法合并成功
    size = (w, h)
    makeVideo(path, size)
