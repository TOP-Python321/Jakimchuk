num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))
num_three = int(input('Введите третье число: '))

sum = 0

#Хотел бы узнать как объеденить все if в 1 условие
if num_one > 0:
    sum += num_one
if num_two > 0:
    sum += num_two
if num_three > 0:
    sum += num_three
    
print(sum)