import json

class Bot():
    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class before running in the class."

    def set_error_list(self):
        pass

    def __init__(self):
        self.setUpClass()
        self.set_error_list()

    def run(self):
        pass

    @classmethod
    def load_config(cls, file_name):
        with open(file_name) as data_file:
            data = json.load(data_file)

        for key in data:
            setattr(cls, key, data[key])

    def close(self):
        pass