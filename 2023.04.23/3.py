numb = int(input("Введите целое число: "))

sum_of_dividers = 0

for i in range(1, numb + 1):
    if (numb % i == 0):
        sum_of_dividers += i
        
print(sum_of_dividers)

# Введите целое число: 50
# 93

# Введите целое число: 60
# 168