from pathlib import Path
import json
import unittest
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel

def remove_persisted_data(path):
    """Remove the persisted data file"""
    try:
        path.unlink()
    except:
        pass

def get_key(obj):
    return f"{obj.__class__.__name__}.{obj.id}"

storage_path = Path(storage._FileStorage__file_path)

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""
    
    def setUp(self):
        storage.objects = {}
        remove_persisted_data(storage_path)
    
    def test_that_storage_starts_without_any_objects_in_memory(self):
        """Test that FileStorage initializes with an empty objects dict"""
        self.assertEqual(storage.objects, {})
        
    def test_that_storage_creates_database_file_if_necessary(self):
        """Test that FileStorage has a predefined file path for JSON file"""        
        self.assertTrue(not storage_path.exists())
        _ = BaseModel()
        storage.save()        
        self.assertTrue(storage_path.exists())
        
   
    def test_that_storage_can_add_objects_to_memory(self):
        """Test adding new objects to FileStorage"""
        with patch.object(storage, 'new', return_value=None):
            obj = BaseModel()
            obj_key = get_key(obj)
        storage.new(obj)
        
        self.assertEqual(storage.objects[obj_key], obj)

    def test_that_storage_can_save_object_to_file_system(self):
        """Test persisting objects to the file system"""
        obj = BaseModel()
        obj_key = get_key(obj)
        storage.save()
        
        with storage_path.open() as database:
            data = json.load(database)
            
        self.assertIn(obj_key, data)

    def test_that_storage_can_reload_objects_from_file_system(self):
        """Test reloading objects from the file system"""
        obj = BaseModel()
        obj_key = get_key(obj)
        storage.save()
        
        storage.objects = {}
        storage.reload()
        
        self.assertEqual(obj.to_dict(), 
                         storage.objects[obj_key].to_dict())

    def test_that_storage_can_show_all_objects(self):
        """Test that the all method returns all stored objects"""
        objs = [BaseModel() for _ in range(5)]
        all_objects = storage.all()
        self.assertEqual(objs, 
                         list(all_objects.values()))

if __name__ == '__main__':
    unittest.main()
