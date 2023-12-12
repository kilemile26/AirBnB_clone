import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestConsole(unittest.TestCase):

    def setUp(self):
        # Reset the FileStorage's __objects dict before each test
        storage.__objects = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        # Test the create command for creating an instance
        with patch('sys.stdin', return_value='BaseModel\n'):
            HBNBCommand().onecmd("create")
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        # Test the show command for displaying an instance
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdin', return_value='BaseModel {}\n'.format(obj_id)):
            HBNBCommand().onecmd("show BaseModel")
        self.assertIn(obj_id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        # Test the destroy command for deleting an instance
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdin', return_value='BaseModel {}\n'.format(obj_id)):
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
        self.assertNotIn(obj_id, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        # Test the all command for displaying all instances
        obj1 = BaseModel()
        obj2 = BaseModel()
        with patch('sys.stdin', return_value='BaseModel\n'):
            HBNBCommand().onecmd("all BaseModel")
        self.assertIn(obj1.id, mock_stdout.getvalue())
        self.assertIn(obj2.id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        # Test the update command for modifying an instance
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdin', return_value='BaseModel {} name "New Name"\n'.format(obj_id)):
            HBNBCommand().onecmd("update BaseModel {} name 'New Name'".format(obj_id))
        self.assertEqual(obj.name, 'New Name')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_dict_command(self, mock_stdout):
        # Test the update command with a dictionary for modifying an instance
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdin', return_value='BaseModel {} {"name": "New Name", "age": 25}\n'.format(obj_id)):
            HBNBCommand().onecmd("update BaseModel {} {}".format(obj_id, '{"name": "New Name", "age": 25}'))
        self.assertEqual(obj.name, 'New Name')
        self.assertEqual(obj.age, 25)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_command(self, mock_stdout):
        # Test the count command for retrieving the number of instances
        obj1 = BaseModel()
        obj2 = BaseModel()
        with patch('sys.stdin', return_value='BaseModel\n'):
            HBNBCommand().onecmd("count BaseModel")
        self.assertIn("2", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        # Test the quit command for exiting the program
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_eof_command(self, mock_stdout):
        # Test the EOF command for exiting the program
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")

if __name__ == '__main__':
    unittest.main()
