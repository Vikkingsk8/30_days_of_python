# Упражнения: Уровень 1
# Создать пустой кортеж
t = ()
print(type(t))
# Создайте кортеж, содержащий имена ваших сестер и братьев (воображаемые братья и сестры подойдут).
sisters = ('anna', 'lisa', 'maria')
brothers = ('faiby', 'sanal')
# Объедините кортежи братьев и сестер и назначьте их братьям и сестрам.
brothers_and_sisters = sisters + brothers
print(brothers_and_sisters)
# Сколько у вас братьев и сестер?
print(len(brothers_and_sisters))
# Измените кортеж братьев и сестер, добавьте имя отца и матери и назначьте его family_members.
brothers_and_sisters = list(brothers_and_sisters)
brothers_and_sisters.append('mother')
brothers_and_sisters.append('father')
family_members = tuple(brothers_and_sisters)
print(family_members)
# Упражнения: Уровень 2
# Распаковать братьев, сестер и родителей из family_members
first, second, third, fourth, fifth, sixth, seventh = family_members
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
# Создайте кортежи фруктов, овощей и продуктов животного происхождения. Объедините три кортежа и присвойте их переменной food_stuff_tp.
meats = ('steak', 'grill')
fruits = ('apple', 'cherry','banana')
vegetables = ('potato', 'tomato','carrot', 'cucumber')
food_stuff_up = meats + fruits + vegetables
print(food_stuff_up)
# Измените кортеж about food_stuff_tp на список food_stuff_lt
food_stuff_up = list(food_stuff_up)
print(food_stuff_up)
# Вырежьте средний элемент или элементы из кортежа food_stuff_tp или списка food_stuff_lt.
avg_elem = len(food_stuff_up)//2
del food_stuff_up[avg_elem]
print(food_stuff_up)
# Вырежьте первые три элемента и последние три элемента из списка food_staff_lt.
first_three_elem = food_stuff_up[:3]
print(first_three_elem)
last_three_elem = food_stuff_up[-3:]
print(last_three_elem)
# Полностью удалить кортеж food_staff_tp
del food_stuff_up
#print(food_stuff_up)
# Проверить, существует ли элемент в кортеже:
# Проверьте, является ли «Эстония» страной Северной Европы.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
# Проверьте, является ли «Исландия» страной Северной Европы.
print('Iceland' in nordic_countries)

