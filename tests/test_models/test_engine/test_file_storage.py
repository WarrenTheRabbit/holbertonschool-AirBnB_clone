# /usr/bin/python3
"""This module contains unit tests for the FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from utils import class_map


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self) -> None:
        self.storage = FileStorage()
        FileStorage._FileStorage__objects.clear()

    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_FileStorage_all_method(self):
        """Tests that the all method of FileStorage works
        as expected
        """
        self.assertEqual(self.storage.all(), {})
        cls = class_map()["BaseModel"]
        obj1 = cls()
        obj2 = cls()
        obj3 = cls()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.assertEqual(len(self.storage.all()), 3)
        self.assertTrue(f"{cls.__name__}.{obj1.id}" in self.storage.all())
        self.assertTrue(f"{cls.__name__}.{obj2.id}" in self.storage.all())
        self.assertTrue(f"{cls.__name__}.{obj3.id}" in self.storage.all())

    def test_FileStorage_reload_method(self):
        """Tests that the reload method of FileStorage works
        as expected
        """
        cls = class_map()["BaseModel"]
        obj = cls()
        self.storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertEqual(obj.to_dict(), self.storage.all()[key].to_dict())
