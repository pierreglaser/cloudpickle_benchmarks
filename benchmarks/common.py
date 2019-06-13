import pickle
from abc import ABCMeta, abstractproperty

import cloudpickle


def transparent_decorator(func):
    # returns a new function that behaves exactly like the input function of
    # the decorator.
    def f(*args, **kwargs):
        return func(*args, **kwargs)
    return f


class CloudpickleTimeBenchmark:
    __metaclass__ = ABCMeta
    number = 1
    repeat = (1, 100, 5)  # repeat benchmark max 100 times or during 5 seconds
    warmup_time = 0.1

    @abstractproperty
    def obj(self):
        raise NotImplementedError

    def setup(self):
        self._pickled_obj = cloudpickle.dumps(self.obj)

    def time_dump(self):
        return cloudpickle.dumps(self.obj)

    def time_load(self):
        return pickle.loads(self._pickled_obj)


class CloudpickleFileSizeBenchmark:
    __metaclass__ = ABCMeta
    number = 1
    repeat = 1

    @abstractproperty
    def obj(self):
        raise NotImplementedError

    def track_dump(self):
        return len(cloudpickle.dumps(self.obj))
