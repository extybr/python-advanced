import logging
import requests
from time import monotonic
from threading import Thread
from multiprocessing import Process
from typing import List, Callable
from database import db

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)

COUNT = range(1, 22)


def process_time(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = monotonic()
        function(*args, **kwargs)
        end = monotonic() - start
        logger.info(f'{function.__name__} >> Done in {end:.4f}')
    return wrapper


def load_starwars(number: int) -> None:
    response: requests.Response = requests.get(f'https://swapi.dev/api/people/{number}')
    if response.status_code != 200:
        return
    i = response.json()
    info = i.get('name', ''), i.get('gender', ''), i.get('birth_year', '')
    db.insert_into_db(info)


@process_time
def standard_request() -> None:
    [load_starwars(i) for i in COUNT]


@process_time
def load_multithreading() -> None:
    threads: List[Thread] = []
    for i in COUNT:
        thread = Thread(target=load_starwars, args=(i, ))
        thread.start()
        threads.append(thread)
    [thread.join() for thread in threads]


@process_time
def load_multiprocessing() -> None:
    processes: List[Process] = []
    for i in COUNT:
        process = Process(target=load_starwars, args=(i, ))
        process.start()
        processes.append(process)
    [process.join() for process in processes]


if __name__ == "__main__":
    standard_request()
    load_multithreading()
    # load_multiprocessing()

# INFO:__main__:standard_request >> Done in 32.0160
# INFO:__main__:load_multithreading >> Done in 4.7500
# INFO:__main__:load_multiprocessing >> Done in 7.9060
