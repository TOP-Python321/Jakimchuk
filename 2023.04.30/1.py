user_email = input('Ввдите ваш Email: ')

if (
        user_email.count('@') == 1
    and user_email[0] != '@'
    # УДАЛИТЬ: проверка избыточна: если метод rfind('.') возвращает значение > -1, то это означает, что подстрока найдена — а это в свою очередь означает что количество вхождений этой же подстроки в исходную > 0, соответственно отдельное выполнение метода count('.') не нужно
    and user_email.count('.') > 0
    and user_email.rfind('.') > user_email.find('@')
):
    print('Да')
else:
    print('Нет')


# Ввдите ваш Email: nikita.222@mail.ru
# Да

# Ввдите ваш Email: nikita.222@mailru
# Нет


# ИТОГ: хорошо — 2/3
