import logging
import requests
from time import monotonic
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool
from typing import Callable
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
def load_pool() -> None:
    with Pool(processes=cpu_count()) as pool:
        pool.map(load_starwars, COUNT)
        # pool.map_async(load_starwars, list(COUNT)).get()


@process_time
def load_threadpool() -> None:
    with ThreadPool(processes=cpu_count()) as pool:
        pool.map(load_starwars, COUNT)
        # pool.map_async(load_starwars, list(COUNT)).get()


if __name__ == "__main__":
    load_pool()
    load_threadpool()

# INFO:__main__:load_pool >> Done in 6.5160
# INFO:__main__:load_threadpool >> Done in 4.8750
