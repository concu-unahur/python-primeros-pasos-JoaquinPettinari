import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

valor = 5

def sumarUno():
    global valor
    time.sleep(.1)
    valor += 1



def multiplicarPorDos():
    global valor
    valor *= 2

t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multiplicarPorDos)

t1.start()
t2.start()

t1.join()
t2.join()

logging.info({valor})

