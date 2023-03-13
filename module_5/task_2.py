import time


class ContextManager:
    """
    Create context manager [timer] using [__enter__] end [__exit__]
    """

    def __init__(self, message: str) -> None:
        self.message: str = message
        self.time_obj: time = time

    def __enter__(self) -> time:
        self.start: time = self.time_obj.time()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("timer: block '{}' executed in {:.3f} sec".format(self.message, self.time_obj.time() - self.start))


if __name__ == '__main__':
    with ContextManager('doing some sleeps'):
        time.sleep(1)
        time.sleep(2)
        time.sleep(3)
