# 💻 Упражнения: День 7
# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Упражнения: Уровень 1
# Найдите длину множества it_companies
print(len(it_companies))
# Добавить «Twitter» в it_companies
it_companies.add('Twitter')
print(it_companies)
# Добавьте сразу несколько ИТ-компаний в набор it_companies
co = {"Yandex", "Puls"}
it_companies.update(co)
print(it_companies)
# Удалить одну из компаний из набора it_companies
it_companies.remove("Yandex")
print(it_companies)

# В чем разница между удалением и отбрасыванием?
#remove(element) - удаляет элемент, но ВЫЗЫВАЕТ ОШИБКУ если элемента нет:
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # ✅ Удалит 3
print(my_set)     # {1, 2, 4, 5}

#my_set.remove(10) # ❌ Вызовет KeyError: 10 discard(element) - удаляет элемент, но НЕ ВЫЗЫВАЕТ ОШИБКУ если элемента нет:
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)  # ✅ Удалит 3
print(my_set)      # {1, 2, 4, 5}
my_set.discard(10) # ✅ Ничего не произойдет, ошибки не будет
print(my_set)      # {1, 2, 4, 5}


# Упражнения: Уровень 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Присоединяйтесь к А и Б
print(A.union(B))
# Найти перекресток A и B
print(A.intersection(B))
# Является ли подмножеством B?
print(A.issubset(B))
# Являются ли A и B непересекающимися множествами?
print(A.isdisjoint(B))
# Соединить А с В и В с А
A1 = A.union(B)
B1 = B.union(A)
print(A1)
print(B1)
# Какова симметричная разница между A и B?
print(A.symmetric_difference(B))
# Полностью удалить наборы
del A
del B
# Упражнения: Уровень 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Преобразуйте возраст в набор и сравните длину списка и набора. Какой из них больше?
age_set = set(age)
print(f'Длинна списка: {len(age)}\nДлинна множества: {len(age_set)}\nСписок {len(age)} - Множество {len(age_set)} = {len(age) - len(age_set)}' )

# Объясните разницу между следующими типами данных: строка, список, кортеж и множество.
# Сравнительная таблица:
# Тип данных	Изменяемость	Упорядоченность	Индексируется	Дубликаты
# Строка	    ❌ Нет	            ✅ Да	    ✅ Да	    ✅ Да
# Список	    ✅ Да	            ✅ Да	    ✅ Да	    ✅ Да
# Кортеж	    ❌ Нет	            ✅ Да	    ✅ Да	    ✅ Да
# Множество	    ✅ Да	            ❌ Нет	    ❌ Нет	    ❌ Нет
# Я учитель и люблю вдохновлять и учить людей. Сколько уникальных слов использовано в предложении? Используйте методы разделения и набора, чтобы получить уникальные слова.
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
s = 'I am a teacher and I love to inspire and teach people'
lst = s.split(' ')
print(lst)
print(f'Всего слов: {len(lst)}')
lst_set = set(lst)
print(lst_set)
print(f'Всего уникальных слов: {len(lst_set)}')