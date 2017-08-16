import os
from unittest import TestCase

from simpledb import SimpleDB


class SimpleDBTest(TestCase):
    path = 'test_json'

    def should_create_test_file(self):
        db = SimpleDB(data_file=self.path)

        self.assertFalse(os.path.exists(self.path))
        db._create_data_file()
        self.assertTrue(os.path.exists(self.path))

    def tearDown(self):
        os.remove(self.path)
