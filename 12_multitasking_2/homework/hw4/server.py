import logging.config
from conf import dict_config
from multiprocessing import Queue
from multiprocessing.pool import ThreadPool
from time import sleep
from datetime import datetime
from flask import Flask

app: Flask = Flask(__name__)

logging.config.dictConfig(dict_config)
logger = logging.getLogger('server')
logger.setLevel('DEBUG')


@app.route('/timestamp/<timestamp>')
def get_timestamp(timestamp: str) -> str:
    timestamp: float = float(timestamp)
    return str(datetime.fromtimestamp(timestamp))


def set_timestamp(cycle):
    for _ in cycle:
        start = datetime.timestamp(datetime.now())
        while datetime.timestamp(datetime.now()) < start + 20:
            logger.info(datetime.timestamp(datetime.now()))
            sleep(1)


def threadpool():
    queue = Queue()
    with ThreadPool(processes=10) as pool:
        queue.put(pool.map(set_timestamp, (range(10), )))
    while not queue.empty():
        queue.get()


if __name__ == '__main__':
    threadpool()
    app.run('127.0.0.1', port=8080, debug=False)
