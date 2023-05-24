quantity = int(input("Укажите количество чисел в последовательности: "))

fibonacci = []
numb = next_numb = 1

while quantity > 0:
    fibonacci.append(numb)
    numb, next_numb = next_numb, numb + next_numb
    quantity -= 1

# ИСПРАВИТЬ: вывод не соответствует требуемому формату
print(fibonacci)


# Укажите количество чисел последовательности: 20
# КОММЕНТАРИЙ: враньё, ваш код выводит не так
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


# ИТОГ: доработать 3/4
