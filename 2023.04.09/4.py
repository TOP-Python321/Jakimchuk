num = int(input())

fr_deg = num // 100
sec_deg = num // 10 % 10
thr_deg = num % 10

# ИСПОЛЬЗОВАТЬ: при таком способе переноса PEP 8 рекомендует выравнивать переносимую строчку по открывающей скобке
print(f'Сумма цифр = {fr_deg + sec_deg + thr_deg} \n'
      f'Произведение цифр = {fr_deg * sec_deg * thr_deg}')


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода
#   https://peps.python.org/pep-0008/


# ИТОГ: отлично — 4/4
