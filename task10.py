"""
Задача 10
Найти количество цифр 5 в числе
    Пример:
        543231235643
        'В числе 2 5-ки.'
"""
# ввод числа и проверка на "число"
num_str = ''
while not num_str.isdigit():
    num_str = input('Введите число: ')

# Зададим цифру для поиска
num_check = 5

num_counter = 0
for i in range(len(num_str)):
    if int(num_str[i]) == num_check:
        num_counter += 1

print(f'В числе {num_str} {num_counter} {num_check}-ки')