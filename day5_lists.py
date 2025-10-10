# # s = str(input())
# # print('is palindrome' if s[::-1] == s else 'is not palindrome')

# Упражнения: Уровень 1
# Объявить пустой список
lst = []
# Объявить список, содержащий более 5 элементов
lst = [1,2,3,4,5,6]
# Найдите длину вашего списка
print(len(lst))
# Получить первый элемент, средний элемент и последний элемент списка
a = len(lst)//2 
print(lst[0],lst[a],lst[-1])
# Объявите список с именем mixed_data_types, вставьте свои(имя, возраст, рост, семейное положение, адрес)
mixed_data_types = ['Viktor', 28, 184, 'married', 'Khimki']
# Объявите переменную списка с именем it_companies и присвойте ей начальные значения Facebook, Google, Microsoft, Apple, IBM, Oracle и Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Распечатать список с помощью print()
print(it_companies)
# Распечатать количество компаний в списке
print(len(it_companies))
# Распечатайте первую, среднюю и последнюю компанию
m = len(it_companies)//2
print(it_companies[0], it_companies[m], it_companies[-1])
# Распечатать список после изменения одной из компаний
it_companies[0] = 'VTB'
print(it_companies)
# Добавить IT-компанию в it_companies
it_companies.append('Yandex')
print(it_companies)
# Вставьте ИТ-компанию в середину списка компаний.
m = len(it_companies)//2
it_companies.insert(m, 'Booble')
print(it_companies)
# Измените название одной из компаний it_companies на заглавное (кроме IBM!)
new_list = []
for i in it_companies:
    if i != 'IBM':
        new_list.append(i.lower())
    else:
        new_list.append(i)
print(new_list)
# Присоединяйтесь к it_companies со строкой '#;'
print('#; '.join(new_list))
# Проверьте, есть ли определенная компания в списке it_companies.
print('Booble' in it_companies)
# Сортировать список с помощью метода sort()
it_companies.sort()
print(it_companies)
# Переверните список в порядке убывания с помощью метода reverse()
it_companies.reverse()
print(it_companies)
# Вырежьте первые 3 компании из списка.
print(it_companies[0:3])
# Вырежьте последние 3 компании из списка.
print(it_companies[-3:])
# Вырежьте среднюю ИТ-компанию или компании из списка.
m = len(it_companies)//2
print(it_companies[m])
# Удалить первую ИТ-компанию из списка
del it_companies[0]
print(it_companies)
# Удалить среднюю ИТ-компанию или компании из списка
m = len(it_companies)//2
del it_companies[m]
print(it_companies)
# Удалить последнюю ИТ-компанию из списка
del it_companies[-1]
print(it_companies)
# Удалить все ИТ-компании из списка
it_companies.clear()
print(it_companies)
# Уничтожить список ИТ-компаний
del it_companies
# Присоединяйтесь к следующим спискам:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# После объединения списков в вопросе 26. Скопируйте объединенный список и присвойте его переменной full_stack, затем вставьте Python и SQL после Redux.
full_stack = front_end + back_end
full_stack.append('Python')
full_stack.append('SQL')
full_stack.append('Redux')
print(full_stack)
# Упражнения: Уровень 2
# Ниже приведен список 10 возрастов учащихся:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Отсортируйте список и найдите минимальный и максимальный возраст.
ages.sort()
print(f'min age: {ages[0]}, max age: {ages[-1]}')
# Добавьте минимальный и максимальный возраст еще раз в список.
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)
# Найдите медианный возраст (один средний элемент или два средних элемента, деленные на два).
mediana = len(ages)//2
print(ages[mediana])
# Найдите средний возраст (сумма всех предметов, деленная на их количество).
s = sum(ages)//len(ages)
print(s)
# Найдите диапазон возрастов (максимум минус минимум)
print(max_age-min_age)
# Сравните значение (мин. - ср.) и (макс. - ср.), используя метод abs()
print(abs(min_age-s), abs(max_age-s))
# Найдите среднюю страну(ы) в списке стран.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
l = len(countries)//2
print(countries[l])
# Разделите список стран на два равных списка, если в первой половине будет хотя бы на одну страну больше.
if len(countries) % 2 == 0:
    # Четное количество - делим пополам
    mid = len(countries) // 2
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    # Нечетное количество - первая половина больше на 1 элемент
    mid = len(countries) // 2 + 1
    first_half = countries[:mid]
    second_half = countries[mid:]

print(first_half)
print(second_half)
# [«Китай», «Россия», «США», «Финляндия», «Швеция», «Норвегия», «Дания»] Распакуйте первые три страны, а остальные — как скандинавские.
c = ['Китай', 'Россия', 'США', 'Финляндия', 'Швеция', 'Норвегия', 'Дания']
first, second, third, *scandinavian = c
print(first)
print(second)
print(third)
print(scandinavian)