import xml
import xml.etree.ElementTree

from .common import transparent_decorator


class SomeClass:
    @classmethod
    def some_classmethod(cls):
        return cls.__name__

    @staticmethod
    def some_staticmethod(x):
        return x

    def some_instancemethod(self):
        pass


def toplevel_function():
    """ Function picklable as a module attribute"""
    pass

some_obj = SomeClass()

# as opposed to SomeClass.some_classmethod/some_staticmethod, those are not
# method objects, but classmethod/staticmethod and are thus pickled using a
# different logic.
classmethod_instance = SomeClass.__dict__['some_classmethod']
staticmethod_instance = SomeClass.__dict__['some_staticmethod']


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


@transparent_decorator
def decorated_function():
    # decorated function becomes a local variable of the transparent_decorator
    # execution scope. It is thus not pickleable as a global.
    pass
