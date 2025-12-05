# Фильтрация только отрицательных и нулевых значений в списке с использованием понимания списка
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0])
# Сведем следующий список списков в одномерный список:
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([number for row in list_of_lists for numbers in row for number in numbers])
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Используя функцию понимания списков, создайте следующий список кортежей:
result = [
    (i, 1, i**1, i**2, i**3, i**4, i**5)
    for i in range(0, 11)
]

for t in result:
    print(t)

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
# Преобразуем следующий список в новый список:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# res = [
#     [country.upper(), country[0:3].upper()]
# ]

res = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for item in countries
    for (country, capital) in item  
]
print(res)

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# Измените следующий список на список словарей:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

res = [
    {'country': country.upper(), 'city': city.upper()}
    for item in countries
    for country, city in item
]
print(res)
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
# Измените следующий список списков на список объединенных строк:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# res = [
#     name, last_name
#     for item in names 
#     for name, last_name in item
# ]
# print(res)
new = []
for name in names:
    new.append(' '.join(name[0]))
print(new)

res = [' '.join(name[0]) for name in names]
print(res)


# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# Напишите лямбда-функцию, которая может вычислить наклон или y-пересечение линейных функций.
# Наклон m = (y2 - y1) / (x2 - x1) для двух точек (x1,y1), (x2,y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None

# y-пересечение b = y - m*x (подставляем любую точку и найденный m)
intercept = lambda x, y, m: y - m * x

m = slope(0, 0, 2, 4)  # m = 2
b = intercept(0, 0, m) # b = 0
print(f"y = {m}x + {b}")  # y = 2x + 0
