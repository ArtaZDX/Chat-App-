import threading
import time


def hello():
	while True:
		print("hello")
		time.sleep(3)

def goodbye():
	while True:
		print("goodbye")
		time.sleep(1)
def hello1():
	while True:
		print("Arta")
		time.sleep(3)

def goodbye1():
	while True:
		print("moghaddasi")
		time.sleep(1)




thread_one = threading.Thread(target=hello)
thread_two = threading.Thread(target=goodbye)
thread_3 = threading.Thread(target=hello1)
thread_4 = threading.Thread(target=goodbye1)


thread_one.start()
thread_two.start()
thread_3.start()
thread_4.start()
