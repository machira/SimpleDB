import json
import os
from collections import Counter


class SimpleDB:
    def __init__(self, data_file='data.json'):
        self.DATA_FILE = data_file

    def write(self, data):
        self._create_data_file_if_not_exists()
        store = self.read()
        store.append(data)

        with open(self.DATA_FILE, 'w') as f:
            txt = json.dumps(store)
            f.write(txt)

    def read(self):
        self._create_data_file_if_not_exists()
        with open(self.DATA_FILE, 'r') as f:
            data = f.read()
            return json.loads(data)

    def query(self, func):
        data = self.read()
        return list(filter(func, data))

    def update(self, test_func, update_func):
        data = self.read()

        def _update_function(x):
            return update_func(x) if test_func(x) else x

        updated_data = list(map(_update_function, data))

        with open(self.DATA_FILE, 'w') as f:
            txt = json.dumps(updated_data)
            f.write(txt)

    def project(self, field):
        data = self.read()
        return list(map(lambda x: x[field], data))

    def countBy(self, field):
        list_for_field = self.project(field)
        frequency = Counter(list_for_field)
        return dict(frequency)

    def _create_data_file_if_not_exists(self):
        if not os.path.isfile(self.DATA_FILE):
            with open(self.DATA_FILE, 'w') as f:
                f.write('[]')

    def delete(self, func):
        result = []
        for item in self.read():
            if not func(item):
                result.append(item)

        with open(self.DATA_FILE, 'w') as f:
            txt = json.dumps(result)
            f.write(txt)

if __name__ == '__main__':
    pass
