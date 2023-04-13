name = input('Введите имя: ');
secname = input('Введите фамилию: ');
date_birth = input('Введите дату вашего рождения: ');

age = 2023 - int(date_birth);

print(secname + " " + name + ",", age);
