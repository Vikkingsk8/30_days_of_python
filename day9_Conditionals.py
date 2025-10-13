# # 💻 Упражнения: День 9
# # Упражнения: Уровень 1
# # Получите данные пользователя, 
# # используя input(«Введите свой возраст:»). 
# # Если пользователю 18 или больше, 
# # оставьте отзыв: Вы достаточно взрослые, чтобы водить машину. 
# # Если меньше 18, оставьте отзыв, чтобы дождаться недостающего количества лет. Вывод:
# a = int(input('Enter your age: '))
# if a >= 18:
#     print('You are old enough to learn to drive.')
# elif a < 18:
#     res = 18 - a
#     print(f'You need {res} more years to learn to drive.')
# # Enter your age: 30
# # You are old enough to learn to drive.
# # Output:
# # Enter your age: 15
# # You need 3 more years to learn to drive.
# # -------------------------------------------------------------------------------------------
# # Сравните значения my_age и your_age, 
# # используя оператор if … else. Кто старше (я или вы)? Используйте input(“Введите ваш возраст: ”), 
# # чтобы получить возраст в качестве входных данных. 
# # Вы можете использовать вложенное условие, 
# # чтобы вывести «year» для разницы в возрасте в 1 год, 
# # «years» для большей разницы и произвольный текст, если my_age = your_age. Вывод:
# b = int(input('Enter your age: '))
# c = int(input('Enter your age: '))
# if b > c:
#     print(f'b person is older then c person {b-c} years')
# elif c > b:
#     print(f'c person is older then b person {b-c} years')
# else:
#     print('both ages equel')


# # Enter your age: 30
# # You are 5 years older than me.
# #----------------------------------------------------------------------------------------------------------
# # Получите два числа от пользователя, 
# # используя приглашение ввода. Если a больше b, 
# # верните значение a больше b, если a меньше b, верните значение a меньше b, иначе a равно b. Выходные данные:
# b = int(input('Enter number one: '))
# c = int(input('Enter number two: '))
# if b > c:
#     print(f'{b} is greater than {c}')
# elif c > b:
#     print(f'{c} is greater than {b}')
# else:
#     print('both numbers equel')
# # Enter number one: 4
# # Enter number two: 3
# # 4 is greater than 3
# #-----------------------------------------------------------------------------------------------------------
# # Упражнения: Уровень 2
# # Напишите код, который выставляет оценки учащимся в соответствии с их баллами:

# # 80-100, A
# # 70-79, B
# # 60-69, C
# # 50-59, D
# # 0-49, F
# grade = 101
# if 80 <= grade >= 100:
#     print('A')
# elif 70 <= grade <= 79: 
#     print('B')
# elif 60 <= grade <= 69:
#     print('C')
# elif 50 <= grade <= 59:
#     print('D')
# else:
#     print('F')
# #---------------------------------------------------------------------------------------------------------------
# # Проверьте, является ли текущее время года осенью, зимой, весной или летом. 
# # Если пользователь ввёл сентябрь, октябрь или ноябрь, то это осень. 
# # Если декабрь, январь или февраль, то это зима. 
# # Если март, апрель или май, то это весна, то это июнь, июль или август, то это лето.
# month = input('Enter your month: ')
# if month in ['сентябрь', 'октябрь', 'ноябрь']:
#     print('autumn')
# elif month in ['декабрь', 'январь', 'февраль']:
#     print('winter')
# else:
#     print('summer')
# #-------------------------------------------------------------------------------------------------------------------
# # Следующий список содержит некоторые фрукты:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = 'cherry'
# if fruit not in fruits:
#     fruits.append(fruit)
#     print('modified list')
# else:
#     print('That fruit already exist in the list')
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
#-------------------------------------------------------------------------------------------------------------------
# Упражнения: Уровень 3
# Вот словарь персон. Можете его модифицировать!
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}
#  * Check if the person dictionary has skills key, 
#  if so print out the middle skill in the skills list.
check = True if person['skills'] else False
if check is True:
    avg = len(person['skills'])//2 
    print(person['skills'][avg])
#-----------------------------------------------------------------------
#  * Check if the person dictionary has skills key, 
#  if so check if the person has 'Python' skill and print out the result.
print('Python' in person['skills'])
#------------------------------------------------------------------------
#  * If a person skills has only JavaScript and React, 
#  print('He is a front end developer'), if the person skills has Node, Python,
#  MongoDB, print('He is a backend developer'), if the person skills has React,
#  Node and MongoDB, Print('He is a fullstack developer'), 
#  else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')
#---------------------------------------------------------------------------------------
#  * If the person is married and if he lives in Finland,
#  print the information in the following format:
#  Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] is True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')