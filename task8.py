"""
Задача 8
Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".
"""

# ввод числа и проверка на "число"
num_str = ''
while not num_str.isdigit():
    num_str = input('Введите число: ')

num_check = "5"

if num_check in num_str:
    print(f'Цифра {num_check} есть в введеном числе {num_str}')
else:
    print(f'Цифры {num_check} нет в введеном числе {num_str}')