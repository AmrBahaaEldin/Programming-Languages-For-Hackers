#!/usr/bin/python3
#cpu and memory       multi processes executed  at the same time
# Library thread
#called named method without ()
import threading
import time
import os
def hi():
    # get processor id ever thread take same id at the time 

    print(os.getpid())
thread1=threading.Thread(target=hi).start()
thread2=threading.Thread(target=hi).start()
thread3=threading.Thread(target=hi).start()
thread4=threading.Thread(target=hi).start()
#join using watting thread keep safe cpu 





print("__________________________________________________")
