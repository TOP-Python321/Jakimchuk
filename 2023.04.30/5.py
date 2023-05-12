dictionary = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

inp = input('Введите слово: ').upper().replace('Ё', 'Е')

points = 0

print(sum(points + k for i in inp for k, v in dictionary.items() if i in v))

# Введите слово: синхрофазотрон
# 29