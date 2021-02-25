import unittest
from main import check_document_existance, get_doc_owner_name, add_new_shelf, delete_doc, get_doc_shelf, \
    show_document_info, documents

from unittest.mock import patch


class TestFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("method setUpClass")

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    @classmethod
    def tearDownClass(cls):
        print("method tearDownClass")

    def test_check_document_existance(self):
        self.assertTrue(check_document_existance('10006'))

    @patch('builtins.input', return_value='10006')
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual('Аристарх Павлов', get_doc_owner_name())

    @patch('builtins.input', return_value='5')
    def test_add_new_shelf(self, mock_input):
        self.assertEqual(('5', True), add_new_shelf())

    @patch('builtins.input', return_value='2')
    def test_negative_add_new_shelf(self, mock_input):
        self.assertEqual(('2', False), add_new_shelf())

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_input):
        self.assertEqual(('11-2', True), delete_doc())

    @patch('builtins.input', return_value='2207 876234')
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual('1', get_doc_shelf())

    def test_show_document_info(self):
        self.assertEqual(('passport', '2207 876234', 'Василий Гупкин'), show_document_info(documents[0]))


if __name__ == '__main__':
    unittest.main()
