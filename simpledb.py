import os


class SimpleDB:
    # DATA_FILE = ''

    def __init__(self, data_file='data.json'):
        self.DATA_FILE = data_file
        # self._create_data_file()

    def create(self, data):
        self._create_data_file()

        pass

    def read(self):
        with open(self.DATA_FILE, 'r') as f:
            return f.read()

    def _create_data_file(self):
        if not os.path.isfile(self.DATA_FILE):
            with open(self.DATA_FILE, 'w') as f:
                f.write('[]')


if __name__ == '__main__':
    print("foo")
