"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def ask_until_true(prompt, function, max_count = 0, err_text = 'Неверно'):
    count = 0
    while True:
        if function(input(prompt)):
            return count
        else:
            print(err_text)
            count += 1
            if max_count > 0 and count >= max_count:
                return count
    pass

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')
ask_until_true('Ввведите год рождения А.С.Пушкина:', lambda x: x == '1799')

# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
ask_until_true('Ввведите день рождения Пушкина:', lambda x: x == '6')
print('Верно!')
