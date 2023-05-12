user_email = input('Ввдите ваш Email: ')

if user_email.count('@') == 1 and user_email[0] != '@' and user_email.count('.') > 0 and user_email.rfind('.') > user_email.find('@'):
    print('Да')
else:
    print('Нет')

# Ввдите ваш Email: nikita.222@mail.ru
# Да

# Ввдите ваш Email: nikita.222@mailru
# Нет