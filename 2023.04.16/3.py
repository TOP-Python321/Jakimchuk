year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:

    print('Да')
    
else:
    print('Нет')
    
# 2024
# Да

# 2023
# Нет