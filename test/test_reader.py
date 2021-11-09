import json
import yaml
import tempfile
import unittest

from yeet.io import reader


class TestReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_data = {"const1": "const2"}

    def test_read_request_file_with_json_file(self):
        _, fpath = tempfile.mkstemp(suffix=".json")
        with open(fpath, "w") as f:
            json.dump(self.file_data, f)
        self.assertEqual(reader.read_request_file(fpath), self.file_data)

    def test_read_request_file_with_yml_file(self):
        _, fpath = tempfile.mkstemp(suffix=".yml")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        self.assertEqual(reader.read_request_file(fpath), self.file_data)

    def test_read_request_file_with_yaml_file(self):
        _, fpath = tempfile.mkstemp(suffix=".yaml")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        self.assertEqual(reader.read_request_file(fpath), self.file_data)

    def test_read_request_file_with_invalid_file(self):
        _, fpath = tempfile.mkstemp(suffix=".asdf")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        with self.assertRaises(reader.UnsupportedFileTypeException):
            reader.read_request_file(fpath)
