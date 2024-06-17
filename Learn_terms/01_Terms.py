
'''
ITERADORES EN PYTHON
'''

'''Example 1'''

# define a list
my_list = [4, 7, 0]

iterator = iter(my_list)

print(next(iterator))  # prints 4

print(next(iterator))  # prints 7

print(next(iterator))  # prints 0


'''Example 2'''

from itertools import count
# create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))


'''Example 3'''

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# 1° forma de ejecutarlo:
for i in PowTwo(4):
    print(i)

# 2° forma de ejecutarlo:
numbers = PowTwo(3)

i = iter(numbers)

print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
print(next(i)) # raises StopIteration exception

# 3° Forma de ejecutarlo:
numbers = PowTwo(3)

i = iter(numbers)
# Usar un bucle while para imprimir todos los elementos
try:
    while True:
        print(next(i))
except StopIteration:
    pass 


'''
GENERADORES EN PYTHON
'''

'''Example 1'''

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

for item in fibonacci(20):
    print(item)


'''Example 2'''

# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)


'''Example 3'''

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))


'''
COMPRENCIÓN DE LISTA
'''

# SINTAXIS: [expression for item in list if condition == True]

'''Example 1'''

numbers = [1, 2, 3, 4, 5]

# create a new list using list comprehension
square_numbers = [num * num for num in numbers]

print(square_numbers)

# Output: [1, 4, 9, 16, 25]


'''Example 2'''

# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]


'''Example 3'''

word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)

# Output: ['o']