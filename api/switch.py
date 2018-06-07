from cronoperate import do
import threading

def switch():
    t1 = threading.Thread(target=do)
    t1.start()