"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""

import functools
import time
from multiprocessing import Process

N = 300000000


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("{}() -> {} sec".format(func.__name__, round(run_time, 2)))
        return value

    return wrapper


@timer
def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


@timer
def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


@timer
def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


@timer
def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


def run_all_calculations_in_parallel():
    procs = []
    proc_simple = Process(target=simple_iteration)
    proc_loops = Process(target=several_for_loops)
    proc_iterate = Process(target=iterate_over_fifteen)
    proc_math = Process(target=math_formula)
    procs.append(proc_simple)
    procs.append(proc_loops)
    procs.append(proc_iterate)
    procs.append(proc_math)
    proc_simple.start()
    proc_loops.start()
    proc_iterate.start()
    proc_math.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()
