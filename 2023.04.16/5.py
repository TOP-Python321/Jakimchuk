first_cell = input('Где стоит ладья?: ')
second_cell = input('Куда ходим?: ')

if first_cell[0] == second_cell[0] or first_cell[1] == second_cell[1]:
    print('Да')
else:
    print('Нет')
    
    
# Где стоит ладья?: a2
# Куда ходим?: a3
# Да