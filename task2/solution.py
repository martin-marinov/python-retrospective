from collections import defaultdict, OrderedDict
from functools import wraps


def groupby(func, seq):
    result = defaultdict(list)
    for x in seq:
        result[func(x)].append(x)
    return result


def compose(outer, inner):
    return lambda *args: outer(inner(*args))


def iterate(func):
    f = lambda *args: args if len(args) > 1 else args[0]
    while True:
        yield f
        f = compose(f, func)


def zip_with(func, *iterables):
    return (func(*ntuple) for ntuple in zip(*iterables))


def memoize(cache_size):
    cached_args = OrderedDict()

    def memoize_decorator(func):
        @wraps(func)
        def wrapper(*args):
            if args not in cached_args:
                cached_args[args] = func(*args)
            result = cached_args[args]
            if len(cached_args) > cache_size:
                cached_args.popitem(last=False)
            return result
        return wrapper
    return memoize_decorator


def cache(func, cache_size):
    return memoize(cache_size)(func)
