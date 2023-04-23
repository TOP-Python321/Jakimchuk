first_cell = input('Введите координату первой клетки: ')
second_cell = input('Введите координату второй клетки: ')

# КОММЕНТАРИЙ: слишком много лишних скобок, здесь они уже объективно затрудняют чтение — помедитируйте ещё раз над таблицей о приоритетах операторов:
#  https://docs.python.org/3/reference/expressions.html#operator-precedence
# КОММЕНТАРИЙ: вам очень повезло, что код символа 'a' является нечётным числом =)
if (((ord(first_cell[0]) + int(first_cell[1])) % 2) == (ord(second_cell[0]) + int(second_cell[1])) % 2):
    print('Да')
else:
    print('Нет')


# a1
# b2
# Да


# ИТОГ: очень хорошо — 4/5
