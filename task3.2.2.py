# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(a=1, b='строка', c=True)
print_params(3, 2, 4)  # Параметры 2 и 4 изменяют  их тип , но функция работает.
#  print_params(18, 'jump', [1, 7], False) # Ошибка False лишний
print_params()
print_params(b=25)  # изменился параметр b
print_params(c=[1, 2, 3]) # изменился параметр c
print()
# Распаковка параметров:
values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}


def print_params(*values_list):
    print(*values_list)


print_params(*values_list)


def print_params(a, b, c):  # второй вариант
    print(a, b, c)


values_list = [1, 'строка', True]
print_params(*values_list)


def print_params(a, b, c):
    print(a, b, c)


values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)


def print_params(**kwargs):
    for kay, value in kwargs.items():
        print(kay, value)


values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)
print()
# Распаковка + отдельные параметры:
values_list_2 = [154, 'bool']


def print_params(*args):
    print(*args)


print_params(*values_list_2)
print_params(*values_list_2, 42)  # работает, добавили 42