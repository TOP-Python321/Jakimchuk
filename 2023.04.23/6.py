ticket_number = input('Введите шестизначный номер билета: ')
sum_1, sum_2 = 0, 0

# КОММЕНТАРИЙ: и тут генераторное выражение такое: "я что, шутка для тебя?"
for i in range(6):
    if i < 3:
        sum_1 += int(ticket_number[i])
    else:
        sum_2 += int(ticket_number[i])   

# ОТВЕТИТЬ: тоже сами раскопали, как используется тернарный оператор?
print('Да' if sum_1 == sum_2 else 'Нет')


# Введите шестизначный номер билета: 123321
# Да

# Введите шестизначный номер билета: 213452
# Нет


# ИТОГ: хорошо, но можно лучше — 3/4
