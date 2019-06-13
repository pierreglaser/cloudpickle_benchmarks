import xml
import xml.etree.ElementTree


class SomeClass:
    @classmethod
    def some_classmethod(cls):
        return cls.__name__

    @staticmethod
    def some_staticmethod(x):
        return x

    def some_instancemethod(self):
        pass


some_obj = SomeClass()


def _func_with_closure_factory():
    a = 1

    def inner():
        return a
    return inner


def _func_using_submodules_factory():
    def inner():
        some_submodule = xml.etree.ElementTree  # use a submodule
        return some_submodule
    return inner


func_with_closure = _func_with_closure_factory()
func_using_submodules = _func_using_submodules_factory()


# builtin-types instances
large_list = list(range(100000))
large_dict = dict(zip(range(100000), range(100000)))
large_tuple = tuple(range(100000))
