import json

class Bot():
    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class before running in the class."

    def __init__(self):
        self.setUpClass()
        self.set_error_list()

    @classmethod
    def load_config(cls, file_name):
        with open(file_name) as data_file:
            data = json.load(data_file)

        for key in data:
            setattr(cls, key, data[key])

    def set_error_list(self):
        pass

    def run(self):
        pass

    def close(self):
        pass