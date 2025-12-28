import os
import pytest
import tempfile


@pytest.fixture
def create_tmp_file():
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
    yield tmp.name
    os.remove(tmp.name)

def test_read(create_tmp_file):
    with open(create_tmp_file, 'r') as file:
        assert 'test data' == file.read()