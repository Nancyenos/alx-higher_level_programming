#!/usr/bin/python3

import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init(self):
        # Test initialization with specific id
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

        # Test initialization with None, should auto-increment id
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        # Test conversion of empty list
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        # Test conversion of list with dictionaries
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, json.dumps(data))

    def test_save_to_file(self):
        # Test saving an empty list
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test saving a list with objects to a file
        b1 = Base(10)
        b2 = Base(20)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            data = json.loads(file.read())
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["id"], 10)
            self.assertEqual(data[1]["id"], 20)

    def test_from_json_string(self):
        # Test conversion from empty json string
        instances = Base.from_json_string("")
        self.assertEqual(instances, [])

        # Test conversion from json string with data
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        json_string = json.dumps(data)
        instances = Base.from_json_string(json_string)
        self.assertEqual(instances, data)

    def test_create(self):
        # Test creating instances from dictionaries
        data = {"id": 1, "name": "John", "age": 30}
        b = Base.create(**data)
        self.assertEqual(b.id, 1)
        self.assertEqual(b.name, "John")
        self.assertEqual(b.age, 30)

    def test_load_from_file(self):
        # Test loading instances from file
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        json_string = json.dumps(data)
        with open("Base.json", "w") as file:
            file.write(json_string)

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].name, "John")
        self.assertEqual(instances[1].name, "Jane")

if __name__ == "__main__":
    unittest.main()

