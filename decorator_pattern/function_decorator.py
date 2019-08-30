import logging

logging.basicConfig(level=logging.INFO)


def logging_decorator(func):
    """记录日志的装饰器"""

    def wrapper(*args, **kwargs):
        func_name = func.__name__
        logging.info(f"{func_name} starting")
        ret = func(*args, **kwargs)
        logging.info(f"{func_name} finished")
        return ret

    return wrapper


def show_info(*args, **kwargs):
    logging.info(f"args: {args} kwargs: {kwargs}")


@logging_decorator
def show_info2(*args, **kwargs):
    logging.info(f"args: {args} kwargs: {kwargs}")


if __name__ == "__main__":
    show_info = logging_decorator(show_info)
    show_info('1', '2', '3', a="a", b="b")
    show_info2('1', '2', '3', a="a", b="b")
