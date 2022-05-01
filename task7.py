"""
Задача 7
Найти произведение цифр числа.
    Пример:
    254314
    Произведение цифр числа - 480(2*5*4*3*1*4)
"""


# ввод числа и проверка на "число"
num_str = ''
while not num_str.isdigit():
    num_str = input('Введите число: ')

# перемножим все числа:
num_product = 1
for i in range(len(num_str)):
    num_product *= int(num_str[i])

# Выведем результат:
print(f'Ваше введеное число {num_str}, произведение всех цифр = {num_product}')
