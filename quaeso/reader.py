import json
import yaml
from functools import partial


class UnsupportedFileTypeException(Exception): pass


def read_request_file(filepath) -> dict:
    if filepath.endswith(".yml") or filepath.endswith(".yaml"):
        loader = partial(yaml.load, Loader=yaml.FullLoader)
    elif filepath.endswith(".json"):
        loader = json.load
    else:
        raise UnsupportedFileTypeException(filepath)

    with open(filepath, "r") as f:
        file_data = loader(f)

    return file_data
