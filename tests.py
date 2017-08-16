import os
from unittest import TestCase

from simpledb import SimpleDB


class SimpleDBTest(TestCase):
    path = 'test.json'

    def setUp(self):
        self.db = SimpleDB(data_file=self.path)

    def test_should_create_test_file(self):
        db = SimpleDB(data_file=self.path)

        self.assertFalse(os.path.exists(self.path))
        db._create_data_file_if_not_exists()
        self.assertTrue(os.path.exists(self.path))

    def test_should_return_empty_list_for_empty_db(self):
        db = SimpleDB(data_file=self.path)

        self.assertEqual([], db.read())

    def test_should_write_to_db(self):
        self.db.write({'a': 1})

        self.assertEqual([{'a': 1}], self.db.read())

    def test_multiple_writes_test(self):
        self.db.write({'a': 1})
        self.db.write({'b': 2})
        self.db.write({'c': 3})

        self.assertEqual([{'a': 1}, {'b': 2}, {'c': 3}], self.db.read())

    def tearDown(self):
        os.remove(self.path)
