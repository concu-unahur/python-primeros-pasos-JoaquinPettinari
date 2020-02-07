import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Thread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        logging.info('Hola1')
        logging.info('Hola2')


t1 = Thread('Joaco')
t1.start()