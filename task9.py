"""
Задача 9
Найти максимальную цифру в числе
Пример:
    354359688
    'Цифра - 9 максимальная в числе 354359688'
"""

# ввод числа и проверка на "число"
num_str = ''
while not num_str.isdigit():
    num_str = input('Введите число: ')

# Для запуска алгоритма примем первую цифру за максимальную
num_max = int(num_str[1])

# Найдем максимальную цифру методом пузырька
for i in range(len(num_str)):
    if int(num_str[i]) > num_max:
        num_max = int(num_str[i])

# Выведем результат:
print(f'Цифра {num_max} - максимальная в числе {num_str}')