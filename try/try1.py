import random
import time
import threading
A=[0,1,2]
B=[]

#小玩具
interval = 5  # 1 秒
def output_values():
    """ 线程函数，用于定时输出 """
    global last_output_time
    while True:
        current_time = time.time()
        if current_time - last_output_time >= interval:
            a=random.choice(A)
            B.append(a)
            last_output_time = current_time
        time.sleep(0.1)
# 初始化上一次输出的时间
last_output_time = time.time()
# 创建并启动线程
thread = threading.Thread(target=output_values)
thread.start()
while True:
    try:
        a=B.pop()
        print(a)
    except:
        continue

    

