def get_function_time(fn):
    import datetime

    def wrapper(*args, **kwargs):
        time1 = datetime.datetime.now().timestamp()
        fn(*args, **kwargs)
        time2 = datetime.datetime.now().timestamp()
        time = (time2 - time1) * 10 ** 3
        print(f'Время выполнения функции {fn.__name__}: {round(time, 3)} миллисекунд')

    return wrapper
