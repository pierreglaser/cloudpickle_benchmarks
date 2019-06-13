from .common import CloudpickleFileSizeBenchmark, CloudpickleTimeBenchmark
from .objects import (SomeClass, func_with_closure, some_obj,
                      func_using_submodules, large_dict, large_list,
                      large_tuple)

BENCH_TYPES = {
    'Time': CloudpickleTimeBenchmark,
    'Size': CloudpickleFileSizeBenchmark
}

OBJECTS = {
    'BoundClassMethod': SomeClass.some_classmethod,
    'BoundStaticMethod': SomeClass.some_staticmethod,
    'BoundInstanceMethod': some_obj.some_staticmethod,
    'UnboundInstanceMethod': SomeClass.some_instancemethod,
    'UnboundClassMethod': SomeClass.__dict__['some_classmethod'],
    'UnboundStaticMethod': SomeClass.__dict__['some_staticmethod'],
    'FuncWithClosure': func_with_closure,
    'FuncUsingSubmodules': func_using_submodules,
    'LargeList': large_list,
    'LargeDict': large_dict,
    'LargeTuple': large_tuple
}

ALL_BENCHMARKS = {}


# Programatically create all benchmarks classes
for bench_type, bench_base_class in BENCH_TYPES.items():
    for obj_name, obj in OBJECTS.items():
        bench_name = '{}{}Benchmark'.format(obj_name, bench_type)
        bench_class = type(bench_name, (bench_base_class, ), {'obj': obj})
        ALL_BENCHMARKS[bench_name] = bench_class

# For the benchmark classes to be discovered by asv, they must be made
# top-level attributes of this module.
globals().update(ALL_BENCHMARKS)
