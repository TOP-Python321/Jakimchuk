quantity = int(input('Укажите количество целых чисел: '))

sum_positive = 0

while quantity != 0:
    numbers = int(input('Введите целое число: '))
    if numbers > 0: 
        sum_positive += numbers
    quantity -= 1

print(sum_positive)


# Укажите количество целых чисел: 5
# Введите целое число: 2
# Введите целое число: -2
# Введите целое число: 5
# Введите целое число: -3
# Введите целое число: 6
# 13


# ИТОГ: отлично — 3/3
