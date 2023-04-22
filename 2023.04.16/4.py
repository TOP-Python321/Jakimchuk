first_cell = input('Введите координату первой клетки: ')
second_cell = input('Введите координату второй клетки: ')

if (((ord(first_cell[0]) + int(first_cell[1])) % 2) == (ord(second_cell[0]) + int(second_cell[1])) % 2):

    print('Да')
    
else:
    print('Нет')
    
# a1
# b2
# Да