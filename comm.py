import functools
import time


def func_time(func):
    """
    计算方法耗时
    :param func:
    :return:
    """

    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.time()
        run_func = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}(), 耗时 {round(end_time - start_time, 5)} s')

        return run_func

    return clocked
