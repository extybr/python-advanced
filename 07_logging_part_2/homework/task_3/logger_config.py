import logging


class CustomHandler(logging.Handler):
    def __init__(self, file_name='', mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        with open(self.file_name + record.levelname + '.log', mode=self.mode) as log:
            log.write(message + '\n')

def write_file():
    formatter = logging.Formatter(
            fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
            datefmt="%y-%m-%d %H:%M:%S"
    )
    file_handler = CustomHandler('calc_')
    file_handler.setFormatter(formatter)
    return file_handler
