num_list = []

while True:
    numbers = int(input('Введите целое число: '))
    if numbers % 7 != 0:
        # КОММЕНТАРИЙ: в более сложных циклах тело цикла будет более длинным и сложным для восприятия, поэтому лучшей практикой будет вывести действия, выполняемые по завершении цикла, за пределы тела цикла
        print(*num_list[::-1])
        break
    num_list.append(numbers)


# Введите целое число: 14
# Введите целое число: 21
# Введите целое число: 35
# Введите целое число: 33
# 35 21 14


# ИТОГ: отлично — 3/3
