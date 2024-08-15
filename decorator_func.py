#! /usr/bin/python3
import time

def timer(func):
    '''decorator func'''

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} ' 
            f'took {(end_time - start_time):.3f} second')
        return result
    return wrapper


@timer
def myFunc(a, b):
    time.sleep(1)
    return a * b

if __name__=="__main__":

    result = myFunc(2, 4)
    print(f'The result is {result}')
