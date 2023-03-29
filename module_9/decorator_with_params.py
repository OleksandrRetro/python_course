import time


def timeit(threshold=0):
    def inner(func):
        print(f"Before function is called with parameter {threshold}.")
        st = time.time()
        func()
        et = time.time()
        elapsed_time = et - st
        if threshold < elapsed_time:
            print('Execution time: {:.3f} seconds'.format(elapsed_time))
        else:
            print("Threshold = ", threshold)

    return inner


@timeit(threshold=12)
def some_heavy_function() -> None:
    print("Inside some_heavy_function")
    time.sleep(3)


@timeit()
def another_function() -> None:
    print("Inside another_function")
