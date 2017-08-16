import json
import os


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

    def _create_data_file_if_not_exists(self):
        if not os.path.isfile(self.DATA_FILE):
            with open(self.DATA_FILE, 'w') as f:
                f.write('[]')


if __name__ == '__main__':
    print("foo")
