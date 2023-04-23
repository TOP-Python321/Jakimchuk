first_cell = input('Укажите первую клетку: ')
second_cell = input('Укажите вторую клетку: ')

if -1 <= ord(first_cell[0]) - ord(second_cell[0]) <= 1 and -1 <= int(first_cell[1]) - int(second_cell[1]) <= 1:
    print('Да')
else:
    print('Нет')


# Укажите первую клетку: a1
# Укажите вторую клетку: b2
# Да

# Укажите первую клетку: a1
# Укажите вторую клетку: c3
# Нет
