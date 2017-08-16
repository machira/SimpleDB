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
        self.db.write({'a': 2})
        self.db.write({'b': 3})

        self.assertEqual([{'a': 1}, {'a': 2}, {'b': 3}], self.db.read())

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)


class QueryTest(TestCase):
    path = 'queries.json'

    def setUp(self):
        self.db = SimpleDB(data_file=self.path)
        for d in [{'a': 1}, {'a': 2}, {'a': 3}]:
            self.db.write(d)

    def _even(self, x):
        return x['a'] % 2 == 0

    def _odd(self, x):
        return not self._even(x)

    def _and(self, x):
        return self._even(x) and self._odd(x)

    def _or(self, x):
        return self._even(x) or self._odd(x)

    def test_even(self):
        expected = [{'a': 2}]
        actual = self.db.query(self._even)

        self.assertEqual(expected, actual)

    def test_odd(self):
        expected = [{'a': 1}, {'a': 3}]
        actual = self.db.query(self._odd)
        self.assertEqual(expected, actual)

    def test_and(self):
        expected = []
        actual = self.db.query(self._and)
        self.assertEqual(expected, actual)

    def test_or(self):
        expected = [{'a': 1}, {'a': 2}, {'a': 3}]
        actual = self.db.query(self._or)
        self.assertEqual(expected, actual)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)


class Update(TestCase):
    path = 'queries.json'

    def setUp(self):
        self.db = SimpleDB(data_file=self.path)
        for d in [{'a': 1}, {'a': 2}, {'a': 3}]:
            self.db.write(d)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_double_even_numbers(self):
        def double(x): return {'a': x['a'] * 2}

        def even(x): return x['a'] % 2 == 0

        self.db.update(even, double)
        expected = [{'a': 1}, {'a': 4}, {'a': 3}]
        actual = self.db.read()
        self.assertEqual(expected, actual)
