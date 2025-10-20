# # main.py file
# # создал файл my_module в котором есть функция generate_full_name
# import my_module # импортируем модуль с функцией
# print(my_module.generate_full_name('Viktor', 'Ermilov')) # вызываем функцию из модуля и получаем результат Viktor Ermilov

# from math import *
# print(sqrt(144))
# import random
# import re
# print(random.random())
# print(random.randint(r'abc', 10))

# 💻 Упражнения: День 12
# Упражнения: Уровень 1
# Напишите функцию, которая генерирует шестизначный/символьный random_user_id.
from random import *
from string import *
def random_user_id():
    s = ''
    charters = ascii_letters + digits
    for _ in range(6):
        s+=choice(charters) 
    
    return s
print(random_user_id())
#-------------------------------------------------------------------------------------
# Измените предыдущую задачу. 
# Объявите функцию с именем user_id_gen_by_user. 
# Она не принимает параметры, но принимает два входных значения с помощью функции input().
# Одно из входных значений — количество символов, а второе — количество идентификаторов,
# которые необходимо сгенерировать.

def user_id_gen_by_user(symbols, ident):
    res = ''
    charters = ascii_letters+digits
    for _ in range(ident):
        for _ in range(symbols):
            res+=choice(charters) 
        res += '\n'
    
    return res

#print(user_id_gen_by_user(symbols=int(input()), ident=int(input())))
#-------------------------------------------------------------------------------------
# Напишите функцию rgb_color_gen. 
# Она будет генерировать RGB-цвета (три значения от 0 до 255 каждое).
def rgb_color_gen():
    lst = []
    for i in range(3):
        lst.append(str(randint(0,255)))
    return f'rgb({lst[0]},{lst[1]},{lst[2]})'

print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
#----------------------------------------------------------------------------------------
# Упражнения: Уровень 2
# Напишите функцию list_of_hexa_colors, 
# которая возвращает любое количество шестнадцатеричных цветов в массиве 
# (шесть шестнадцатеричных чисел, записанных после #. Шестнадцатеричная система счисления состоит из 16 символов,
# 0-9 и первых 6 букв алфавита, af. Проверьте задание 6 для примеров вывода).
def list_of_hexa_colors():
    lst = []
    charters = digits + 'ABCDEF'
    for _ in range(6):
        res = '#'
        for _ in range(6):
            res+=choice(charters) 
        lst.append(res)
    
    return lst
print(list_of_hexa_colors())
# Напишите функцию list_of_rgb_colors, 
# которая возвращает любое количество цветов RGB в массиве.
def list_of_rgb_colors():
    lst = []
    for _ in range(3):
        lst.append(f'rgb({randint(0,255)}, {randint(0,255)},{randint(0,255)})')
    return lst

print(list_of_rgb_colors())
#------------------------------------------------------------------------------------
# Напишите функцию generate_colors, 
# которая может генерировать любое количество цветов в формате HEX или RGB.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(mode, count):
    lst = []
    if mode == 'hexa':
        charters = digits + 'ABCDEF'
        for _ in range(count):
            res = '#'
            for _ in range(6):
                res+=choice(charters) 
            lst.append(res)
        return lst
    else:
        for _ in range(3):
            lst.append(f'rgb({randint(0,255)}, {randint(0,255)},{randint(0,255)})')
        return lst

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))
#-------------------------------------------------------------------------------
# Упражнения: Уровень 3
# Вызовите функцию shuffle_list, 
# она принимает список в качестве параметра и возвращает перемешанный список.
def shuffle_list(lst):
    shuffle(lst)
    return lst
print(shuffle_list(['v','f','a','t',1,23,4]))
#---------------------------------------------------------------------------------
# Напишите функцию, 
# которая возвращает массив из семи случайных чисел в диапазоне от 0 до 9.
# Все числа должны быть уникальными.
def random_digits():
    lst = []
    while len(lst) < 7:
        elem = randint(0, 9)
        if elem not in lst:
            lst.append(elem)

    return lst

print(random_digits())
    