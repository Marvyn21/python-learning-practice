'''
learning about function definition
def greetings_function(name, age):
    print('Welcome ' +name +  ' You are '+str(age)+ ' years old')

name = input('Enter your name: ')
age = input('Enter your age: ')
greetings_function(name, age)

learning the return statement
def add_numbers(num1, num2):
    return num1+num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(add_numbers(num1,num2))

if statements

a = False
b = 5

if a == b:
    print('A is true')
elif a == False:
    print('A is false')
else:
    print('A is none of the two')

num = int(input('Enter a number: '))

if num%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

DICTIONARIES IN PYTHON

my_dict = {
    'name': 'John',
    'age': 45,
    'is_tall': True,
    'nationality': 'Asian',
    'Qualification': 'College degree',
    'friends': ['Peter', 'Alex', 'Paul']
}
x = my_dict['name']

print(x)

print(type(my_dict))

WHILE LOOP
i = 1
while i <= 6:
    print(i)
    i += 1

2D LISTS AND NESTED LOOPS
my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for lists in my_list:
    for row in lists:
        print(row)
'''

# TRY EXCEPT
'''
try:
    x = int(input('Input an integer: '))
    print(x)countries
except :
    print('Something went wrong')
finally: 
    print('try except finished')
'''

# READING FILES IN PYTHON
'''
country_file = open('the_new.py', 'w')
country_file.write('print(\'This is the new file\')')
country_file.close()
'''

# CLASSES AND OBJECTS 
''' 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input('Enter your name: ')
age = input('Enter your age: ')
p1 = person(name, age)
print(p1.name)
print(p1.age)
'''

# INHERITANCE
''' 
from the_new import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)
''' 
