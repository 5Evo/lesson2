# ввод числа и проверка на "число"
num_str = ''
while not num_str.isdigit():
    num_str = input('Введите число: ')

# просуммируем все числа:
num_sum = 0
for i in range(len(num_str)):
    num_sum += int(num_str[i])

# Выведем результат:
print(f'Ваше введеное число {num_str}, сумма всех цифр=, {num_sum}')
