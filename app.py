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