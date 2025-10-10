# # print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# # print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
# # print('Day 1\t5\t5')
# # print('Day 2\t6\t20')
# # print('Day 3\t5\t23')
# # print('Day 4\t1\t35')
# # print('This is a backslash  symbol (\\)') # To write a backslash
# # print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# # Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
# print(formated_string)
# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"


print("==  exercise 1 ==")
a = 'Thirty'
b = 'days'
c = 'of'
d = 'Python'
l = [a,b,c,d]
l1 = ['Coding', 'For', 'All']
print(' '.join(l))
print(' '.join(l1))

print('=== exersice 2 ===')
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
#company = company[7:]
#print(company.index('Coding'))
print(company.find('Coding'))
#print(company.replace('Coding', 'Python'))
print(company.split())
print("=== exerecise 3 ===")
s = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(s.split(','))
print(company.rfind('l'))
print(company[0])
s = 'Вы не можете закончить предложение словами «потому что потому что потому что» — это союз'
print(s.replace('«потому что потому что потому что»', ''))
print(company.startswith('Coding'))
print(company.startswith('coding'))
print('python_t'.isidentifier())
print('30python_days'.isidentifier())
print('=== exercise 4 ===')
l = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(l))
print('I am enjoying this challenge.\nI just wonder what is next.')
print(f'Name\tAge\tCountry\tCity\nAsabeneh 250\tFinland\tHelsinki')
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')
print('====  final exersice =====')
import math as math
a = 8
b = 6
print(f'''{a} + {b} = {a+b}
{a} - {b} = {a-b}
{a} * {b} = {a*b}
{a} / {b} = {math.fmod(a,b)}
{a} % {b} = {a%b}
{a} // {b} = {a//b}
{a} ** {b} = {math.pow(a,b)}''')


