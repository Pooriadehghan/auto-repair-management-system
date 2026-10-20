from functools import wraps
from utils.logger import Logger


def exception_handling(function):
    @wraps(function)
    def inner(*args, **kwargs):
        params = args[1:] if len(args) > 1 else args
        call_args = f"{params}" if not kwargs else f"{params}, {kwargs}"

        try:
            output = function(*args, **kwargs)
            if "find" not in function.__name__:
                result_to_log = output[1] if isinstance(output, (tuple, list)) and len(output) > 1 else output
                Logger.info(f"{function.__qualname__}{call_args} [RETURNED] : {result_to_log}")
            else:
                Logger.info(f"{function.__qualname__}{call_args}")
            return output
        except Exception as e:
            Logger.error(f"{function.__qualname__}{call_args} [RAISED EXCEPTION] : {e}")
            return False, str(e)

    return inner


def log(function):
    @wraps(function)
    def inner(*args, **kwargs):
        params = args[1:] if len(args) > 1 else args
        call_args = f"{params}" if not kwargs else f"{params}, {kwargs}"

        output = function(*args, **kwargs)
        if "find" not in function.__name__:
            result_to_log = output[1] if isinstance(output, (tuple, list)) and len(output) > 1 else output
            Logger.info(f"{function.__qualname__}{call_args} [RETURNED] : {result_to_log}")
        else:
            Logger.info(f"{function.__qualname__}{call_args}")
        return output

    return inner
