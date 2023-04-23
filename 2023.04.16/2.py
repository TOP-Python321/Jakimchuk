num_one = int(input('Введите делимое число: '))
num_two = int(input('Введите делитель число: '))

if num_one % num_two == 0:
    print(f'{num_one} делится на {num_two} нацело \n'
          f'частное: {(num_one // num_two)}')
else:
    print(f'{num_one} не делится на {num_two} нацело \n'
          f'неполное частное: {num_one // num_two} \n'
          f'остаток: {num_one % num_two}')


# 10 делится на 5 нацело
# частное: 2

# 12 не делится на 5 нацело
# неполное частное: 2
# остаток: 2
