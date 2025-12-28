import L_4

def test_read():
    file_name = L_4.create_file()
    try:
        with open(file_name, 'r') as file:
            assert 'test data' == file.read()
    finally:
        L_4.delete_file_after_test(file_name)


def test_update():
    file_name = L_4.create_file()
    try:
        with open(file_name, 'a') as file:
            file.write('test2')
        with open(file_name, 'r') as file:
            assert 'test2' in file.read()
    finally:
        L_4.delete_file_after_test(file_name)


def test_delete():
    file_name = L_4.create_file()
    L_4.os.remove(file_name)
    assert not L_4.os.path.isfile(file_name)