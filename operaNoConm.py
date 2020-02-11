import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

valor = 5

lock = threading.Lock()
lock2 = threading.Lock()

def sumarUno():
    global valor
    global lock
    

    try:
        valor += 1 

    finally:
        lock.release()


def multiplicarPorDos():
    global valor
    global lock
    global lock2

    
    lock.acquire()

    try:
        valor *= 2
    finally:
        lock.release()



t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multiplicarPorDos)

lock.acquire()

t2.start()
t1.start()

t2.join()

"""
valor = 5

def sumarUno():
    global valor
    valor += 1



def multiplicarPorDos():
    global valor
    time.sleep(.1)
    valor *= 2

t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multiplicarPorDos)

t2.start()
t1.start()

t2.join()
"""
logging.info({valor})

