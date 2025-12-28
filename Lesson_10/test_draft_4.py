import os
import tempfile
from typing import Optional

file_name: Optional[str] = None


def setup_function():
    global file_name
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
        file_name = tmp.name


def teardown_function():
    if os.path.isfile(file_name):
        os.remove(file_name)


def test_read():
    with open(file_name, 'r') as file:
        assert 'test data' == file.read()


def test_update():
    with open(file_name, 'a') as file:
        file.write('test2')
    with open(file_name, 'r') as file:
        assert 'test2' in file.read()


def test_delete():
    os.remove(file_name)
    assert not os.path.isfile(file_name)