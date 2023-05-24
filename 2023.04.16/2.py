num_one = int(input('Введите делимое число: '))
num_two = int(input('Введите делитель число: '))

quotient = int(num_one // num_two)
remainder = int(num_one % num_two)

# СДЕЛАТЬ: подумайте и перепишите код так, чтобы обойтись только одним блоком if
# if num_one % num_two == 0:
    # print(f'{num_one} делится на {num_two} нацело \n'
         # f'частное: {num_one // num_two}')
# else:
   # print(f'{num_one} не делится на {num_two} нацело \n'
         # f'неполное частное: {num_one // num_two} \n'
         # f'остаток: {num_one % num_two}')

# ИСПРАВИТЬ: почти получилось. ещё бы всю строку не генерировать два раза, как бы это сделать, м?)
answer = (f'{num_one} делится на {num_two} нацело \n'
          f'частное: {quotient}')
if remainder:
    answer = (f'{num_one} не делится на {num_two} нацело \n' 
              f'неполное частное: {quotient} \n'
              f'остаток: {remainder}')

print(answer)


# 10 делится на 5 нацело
# частное: 2

# 12 не делится на 5 нацело
# неполное частное: 2
# остаток: 2


# ИТОГ: отлично — 3/3
