# /usr/bin/python3
"""This module contains unit tests for the FileStorage class"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models import storage
from utils import class_map


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self) -> None:
        self.resetStorage()

    def tearDown(self) -> None:
        self.resetStorage()

    def resetStorage(self):
        """Resets storage data"""
        FileStorage._FileStorage__objects = {}
        filepath = FileStorage._FileStorage__file_path
        if os.path.isfile(filepath):
            os.remove(filepath)

    def test_storage_is_instantiated(self):
        """Test that storage is instantiated and of correct type"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_file_path_is_used_to_create_file(self):
        """Tests that the private variable value for attribute __file_pat
        is used to create a matching file
        """
        self.assertTrue(
            hasattr(FileStorage, "_FileStorage__file_path"))
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test__objects_exists_and_is_correctly_updated(self):
        """Tests that the private varible __object exists
        and is properly updated when objects are created
        """
        self.assertTrue(
            hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(
            str(type(FileStorage._FileStorage__objects)), "<class 'dict'>")
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_FileStorage_all_method(self):
        """Tests that the all method of FileStorage works
        as expected
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        cls = class_map()["BaseModel"]
        obj1 = cls()
        obj2 = cls()
        obj3 = cls()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        self.assertEqual(len(storage.all()), 3)
        self.assertTrue(f"{cls.__name__}.{obj1.id}" in storage.all())
        self.assertTrue(f"{cls.__name__}.{obj2.id}" in storage.all())
        self.assertTrue(f"{cls.__name__}.{obj3.id}" in storage.all())

    def test_FileStorage_new_method(self):
        """Tests that the new method of FileStorage works
        as expected
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        cls = class_map()["BaseModel"]
        obj = cls()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_FileStorage_save_method(self):
        """Tests that the save method of FileStorage works
        as expected
        """
        cls = class_map()["BaseModel"]
        obj = cls()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        storage.save()
        obj_dict = {key: obj.to_dict()}
        with open(
            FileStorage._FileStorage__file_path, "r", encoding="utf-8"
        ) as f:
            self.assertEqual(f.read(), json.dumps(obj_dict))

    def test_FileStorage_reload_method(self):
        """Tests that the reload method of FileStorage works
        as expected
        """
        cls = class_map()["BaseModel"]
        obj = cls()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        storage.save()
        storage.reload()
        self.assertEqual(obj.to_dict(), storage.all()[key].to_dict())
