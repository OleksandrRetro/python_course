import time
import unittest

from module_9.decorator_with_params import timeit


class TestMyDecorator(unittest.TestCase):

    def test_decorator_with_parameter(self):
        @timeit(121)
        def my_function():
            time.sleep(1)
            print("Hello from my_function.")


if __name__ == '__main__':
    unittest.main()
