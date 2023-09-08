import logging
import random
import threading
import time

BOX_TICKETS: int = 10
TOTAL_TICKETS: int = 50 - BOX_TICKETS

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger: logging.Logger = logging.getLogger(__name__)

class Director(threading.Thread):
    def __init__(self, semaphore):
        super(Director, self).__init__()
        self._semaphore = semaphore
        logger.info('Director started work')

    def run(self) -> None:
        global TOTAL_TICKETS, BOX_TICKETS
        while TOTAL_TICKETS:
            if BOX_TICKETS < 4:
                with self._semaphore:
                    tickets_print = 10 - (BOX_TICKETS % 10)
                    if tickets_print > TOTAL_TICKETS:
                        tickets_print = TOTAL_TICKETS
                    BOX_TICKETS += tickets_print
                    TOTAL_TICKETS -= tickets_print
                    logger.info(f'Director put {tickets_print} new tickets')
        logger.info('Director stops work, not more tickets')


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore) -> None:
        super().__init__()
        self._semaphore = semaphore
        self.tickets_sold: int = 0
        logger.info('Seller started work')

    def run(self) -> None:
        global TOTAL_TICKETS, BOX_TICKETS
        is_running: bool = True
        while is_running:
            self.random_sleep()
            with self._semaphore:
                if BOX_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                BOX_TICKETS -= 1
                logger.info(f'{self.name} sold one;  {BOX_TICKETS} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self) -> None:
        time.sleep(random.randint(0, 1))


def main():
    semaphore: threading.Semaphore = threading.Semaphore()
    director = Director(semaphore=semaphore)
    director.start()
    sellers = [director]
    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)
    for seller in sellers:
        seller.join()

    tickets_sold = 0
    for seller in sellers:
        if seller != director:
            tickets_sold += seller.tickets_sold
    print('Продано:', tickets_sold, 'билетов')


if __name__ == '__main__':
    main()
