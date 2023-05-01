quantity = int(input("Укажите количество чисел в последовательности: "))

fibonacci = []
numb = next_numb = 1

while quantity > 0:
    fibonacci.append(numb)
    numb, next_numb = next_numb, numb + next_numb
    quantity -= 1
    
print(fibonacci)

# Укажите количество чисел последовательности: 20
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765