import cv2
import os

cap = cv2.VideoCapture('C:\\Users\\pc\\Music\\MV\\ウォルピスカーター-泥中に咲く(超清).mp4')
out_dir = 'D:\\pythonProject\\resource\\result'
skip_num = 5*16     # 跳帧频率


if not os.path.exists(out_dir):
    os.makedirs(out_dir)

count=0

frame_count = 0

all_frames=[]
while(True):
    ret, frame = cap.read()
    if ret is False:
        break
    frame_count = frame_count + 1
    if frame_count % skip_num == 0:
        print(frame_count)
        frame_name = str(frame_count) + '.jpg'
        path = os.path.join(out_dir,frame_name)
        cv2.imwrite(path,frame)



