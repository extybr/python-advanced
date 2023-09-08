from threading import Thread
from queue import PriorityQueue
from time import sleep
from random import uniform

queue = PriorityQueue()


class Producer(Thread):
    def __init__(self):
        super().__init__()
        print('Producer: Running')

    def run(self):
        global queue
        for item in range(0, 10):
            queue.put(item)
            time = self.random_sleep()
            sleep(time)
            print(f'Putting Task(priority={item}) | sleep({time})')
        print('Producer: Done')

    @staticmethod
    def random_sleep():
        return uniform(0.5, 0.6)


class Consumer(Thread):
    def __init__(self):
        super().__init__()
        print('Consumer: Running')

    def run(self):
        global queue
        while queue:
            item = queue.get()
            time = self.random_sleep()
            sleep(time)
            print(f'running Task(priority={item}) | sleep({time})')
            queue.task_done()

    @staticmethod
    def random_sleep():
        return uniform(0.6, 0.7)


producer = Producer()
Thread(target=producer.run).start()
consumer = Consumer()
Thread(target=consumer.run, daemon=True).start()
queue.join()
print('Consumer: Done')
