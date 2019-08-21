"""Data loading utility class."""
from yaml import load, SafeLoader
from yaml.scanner import ScannerError

import sys

def file_contents(filename):
    """File reading function with Exception handling"""
    contents = None

    with open(filename, "r") as file:
        contents = file.read()

    return(contents)


def yaml_loader(yaml_data):
    """Inflate the provided YAML and return it as a Python structure."""
    yaml = None

    try:
        inflated_yaml = load(yaml_data, Loader=SafeLoader)
    except ScannerError as error:
        print(f"Invalid YAML: [{error}]", file=sys.stderr)
        sys.exit(1)

    return(inflated_yaml)
