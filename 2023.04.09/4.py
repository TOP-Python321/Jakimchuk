num = int(input())

fr_deg = num // 100
sec_deg = num // 10 % 10
thr_deg = num % 10

print(f'Сумма цифр = {fr_deg + sec_deg + thr_deg} \n'
f'Произведение цифр = {fr_deg * sec_deg * thr_deg}')