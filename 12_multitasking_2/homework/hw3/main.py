from time import sleep
from threading import Semaphore, Thread

semaphore: Semaphore = Semaphore()
FLAG = True


def start_thread_1() -> None:
    while FLAG:
        semaphore.acquire()
        print(1)
        semaphore.release()
        sleep(0.25)


def start_thread_2() -> None:
    while FLAG:
        semaphore.acquire()
        print(2)
        semaphore.release()
        sleep(0.25)



thread_1: Thread = Thread(target=start_thread_1)
thread_2: Thread = Thread(target=start_thread_2)
try:
    thread_1.start()
    thread_2.start()
    while True:
        ...
except KeyboardInterrupt:
    FLAG = False
    print('\nReceived keyboard interrupt, quitting threads.')
    exit(1)
