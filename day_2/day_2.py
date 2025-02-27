# Day 2 - 30DaysOfPython

# Built in Functions

print('Hello World')                # Hello World
len('Hello World')                  # 11
type('Hello World')                 # <class 'str'>
str(10)                             # '10'
int(10)                             # 10
float(10)                           # 10.0
input('Enter your name: ')          # Takes user input Enter your name: Maria and prints 'Maria'

# Variables in Python

first_name = 'Ava'
last_name = 'Smith'
country = 'New Zealand'
city = 'Auckland'
age = '20'
is_married = False
skills = ['HTML, PHP, CSS']
person_info = {
    'firstname' : 'Ava',
    'lastname' : 'Smith',
    'country' : 'New Zealand',
    'city' : 'Auckland'
}

print('Hello, World!')              # is an argument
print('Hello', ',', 'World', '!')   # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!'))         # only take 1 argument = 13

# Printing the values stored in the variables

print('First name: ', first_name)
print('First name length: ', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person Information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Ava', 'Smith', 'New Zealand', 'Auckland', 20, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Getting user input

first_name = input('What is your name? ')
age =input('How old are you? ')

print(first_name)
print(age)

# Converting one data type to another

# int to float
num_int = 10
print('num_int ', num_int)               # 10
num_float = float(num_int)
print('num_float ', num_float)           # 10.0

# float to int
gravity = 9.81
print(int(gravity))                      # 9

# int to str
num_int = 10
print(num_int)                           # 10
num_str = str(num_int)
print(num_str)                           # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num float: ', num_float)          #10.6
num_int = int(num_float)
print('num int ', int(num_int))          #10

# str to list
first_name = 'Ava'
print(first_name)                        # 'Ava'
first_name_to_list = list(first_name)
print(first_name_to_list)                # ['A', 'v', 'a,']

# Activity

# Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...


# Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...


# Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j

#to commit changes