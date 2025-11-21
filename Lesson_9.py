def decorator_for_function(func):
    def wrapper():
        print("Работа до вызова функции")
        func()  # вызов функции
        print("Работа после вызова функции")
    return wrapper

def my_func():
    """Функция которая чего-то делает"""
    print("Функция которая чего-то делает")

f = decorator_for_function(my_func)
f()