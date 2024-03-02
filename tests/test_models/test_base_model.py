#!/usr/bin/python3
"""Modlule contains unit tests for BaseModel class"""
import os
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Class implements tests for the BaseModel class"""

    def setUp(self) -> None:
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self) -> None:
        """Contains operations to execute after tests are run"""
        pass

    def test_instance_can_be_created(self):
        """Tests the initialization of the BaseModel class with no arguments
        """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        b.name = "BaseModel instance"
        b.number = 10
        self.assertEqual(b.name, "BaseModel instance")
        self.assertEqual(b.number, 10)

    def test_instance_contains_id_attribute(self):
        """Test that an instance contains id attribute"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertTrue(isinstance(b1.id, str))
        self.assertTrue(isinstance(b2.id, str))
        self.assertNotEqual(b1.id, b2.id)

    def test_instance_contains_created_at_attribute(self):
        """Test that an instance contains created_at attribute"""
        b = BaseModel()
        self.assertEqual(str(type(b.created_at)),
                         "<class 'datetime.datetime'>")

    def test_instance_contains_updated_at_attribute(self):
        """Test that an instance contains updated_at attribute"""
        b = BaseModel()
        self.assertEqual(str(type(b.updated_at)),
                         "<class 'datetime.datetime'>")

    def test_to_dict_(self):
        """Test that to_dict method works as expected"""
        b = BaseModel()
        b.name = "BaseModel instance"
        b.number = 10
        b_dict = b.to_dict()
        self.assertEqual(str(type(b_dict)), "<class 'dict'>")
        self.assertIn("name", b_dict)
        self.assertIn("number", b_dict)
        self.assertEqual(b_dict["name"], "BaseModel instance")
        self.assertEqual(b_dict["number"], 10)

    def test_initialization_with_kwargs(self):
        """Creating instance with keyword arguments works
        as expected"""

        b = BaseModel()
        b_dict = b.to_dict()
        b_dup = BaseModel(**b_dict)
        self.assertFalse(b_dup is b)

    def test_string_representation(self):
        """ Check that the __str__ method override exists
        and produces the correct output"""
        b = BaseModel()
        b_str = b.__str__()
        expected_str = f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(expected_str, b_str)

    def test_save_method(self):
        """Test that the save method works as expected"""
        b = BaseModel()
        b.save()
        # FileStorage._FileStorage__objects = {}
        file_path = FileStorage._FileStorage__file_path
        objects = FileStorage._FileStorage__objects
        obj_str = json.dumps({k: v.to_dict() for k, v in objects.items()})
        self.assertTrue(os.path.isfile(file_path))
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
            self.assertEqual(obj_str, file_content)


if __name__ == "__main__":
    unittest.main()
