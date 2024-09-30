#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Load the compiled module 'hidden_4.pyc'
    module_name = "hidden_4"
    spec = importlib.util.spec_from_file_location(module_name,
            "./hidden_4.pyc")
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)

    # Get the list of names defined in the module
    names = dir(hidden_module)

    # Print names that do not start with '__'
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
