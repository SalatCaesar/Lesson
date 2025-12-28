import os
import tempfile


def create_file():
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
        return tmp.name


def delete_file_after_test(file_name):
    os.remove(file_name)