import unittest


class TestImports(unittest.TestCase):
    
    def test_BaseModel_imports_model_and_storage(self):
        from models import storage, BaseModel
        
        self.assertTrue(storage)
        self.assertTrue(BaseModel)

if __name__ == '__main__':
    unittest.main()
