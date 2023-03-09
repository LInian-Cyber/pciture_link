import time
import threading
import queue

q = queue.Queue(1)
def createTimer():
    t = threading.Timer(0.1, repeat)
    t.start()

def repeat():
    q.put(time.strftime('%H:%M:%S', time.localtime()),True,None)
    # 发送时间
    createTimer()


createTimer()
while (True):
    if q.full():
        print("hello,已经开始通讯任务，通讯的内容为"+q.get(True,None))
    else:
        print("hello,暂时还没用通讯任务")
    # time.sleep(0.1)