

from functools import lru_cache
import time

def timer(func: callable):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        print(f'start {start_time}')
        result = func(*args, **kwargs)
        print('toma')
        end_time = time.perf_counter()
        print(f'end {end_time}')
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        if total_time>4:
            raise Exception("aborted. try again later")
        return result
    return wrapper


@lru_cache
@timer
def do_things():
    time.sleep(3)

@timer
def execute()->None:
    do_things()
    do_things()
    do_things()
    time.sleep(1)



if __name__=="__main__":
    execute()