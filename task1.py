import inspect
import sys
import time
from pprint import pprint

import example


class IntrospectionReflectionTool:
    """Inspection and reflection"""
    @staticmethod
    def introspect_code(code):
        """Code inspection"""
        print("Inspection >>>")

        names = ()
        for name, data in inspect.getmembers(code, inspect.isclass):
            names += (name,)
            print(name + ": " + str(data))

        print("-" * 75)

        funcs = ()
        for name, data in inspect.getmembers(code, inspect.isfunction):
            funcs += (name,)
            print(name + ": " + str(data))

        print("-" * 75)

        if len(names) != 0:
            for name in names:
                print(inspect.getmro(code.__getattribute__(name)))

            print("-" * 75)

            for name in names:
                print(name + " functions:")
                pprint(inspect.getmembers(code.__getattribute__(name), inspect.isfunction))

            print("-" * 75)

            for name in names:
                print(f"{name}.__doc__: ", inspect.getdoc(code.__getattribute__(name)))
        else:
            print("No classes")

        print("-" * 75)

        if len(funcs) != 0:
            for name in funcs:
                print(f"{name}.__doc__: ", inspect.getdoc(code.__getattribute__(name)))

            print("-" * 75)

            for name in funcs:
                print(f"'{name}' attr:", inspect.signature(code.__getattribute__(name)))
        else:
            print("No functions")

        print("-" * 75)

    @staticmethod
    def reflect_proces(code):
        """Code reflection"""
        print("Reflection >>>")
        print("Memory size in bites:", sys.getsizeof(code))

        start_time = time.time()
        with open(f"{code.__name__}.py") as file:
            exec(file.read())

        print("Execution time:")
        print("\t--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    introspection = IntrospectionReflectionTool()

    introspection.introspect_code(example)
    introspection.reflect_proces(example)
