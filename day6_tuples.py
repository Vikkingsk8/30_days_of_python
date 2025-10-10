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