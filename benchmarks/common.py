import pickle
from abc import ABCMeta, abstractproperty

import cloudpickle


class CloudpickleTimeBenchmark:
    __metaclass__ = ABCMeta
    number = 1
    repeat = 100
    warmup_time = 0.1
    pretty_name = "OK"

    @abstractproperty
    def obj(self):
        raise NotImplementedError

    def setup(self):
        self._pickled_obj = cloudpickle.dumps(self.obj)

    def time_dump(self):
        return cloudpickle.dumps(self.obj)

    def time_load(self):
        return pickle.loads(self._pickled_obj)


class CloudpickleFileSizeBenchmark():
    __metaclass__ = ABCMeta
    number = 1
    repeat = 1

    @abstractproperty
    def obj(self):
        raise NotImplementedError

    def track_dump(self):
        return len(cloudpickle.dumps(self.obj))
