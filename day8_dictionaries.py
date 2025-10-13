# Create an empty dictionary called dog
dog = {}
print(type(dog))
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Боня'
dog['color'] = 'white'
dog['breed'] = 'chihuahua'
dog['legs'] = 4
dog['age'] = 2
print(dog)
# Create a student dictionary and add first_name, 
# last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student = {}
student.update({'first_name': 'Viktor',
                'last_name': 'Vladimirovich',
                'gender': 'm', 'age': 28, 'marital status': 'married',
                'skills': ['SQL', 'Python'],
                'country': 'Russia',
                'city': 'Moscow',
                'address': 'Pushkin st'
                })
# Get the length of the student dictionary
print(student)
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('ML')
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
del student['address']
print(student)
# Delete one of the dictionaries
del student
print(student)














































