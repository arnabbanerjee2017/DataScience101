# Advanced Function Concepts.

# Recursion.
def my_sum(my_list):  # The parameter will only take numbers otherwise raise exception.
    print(my_list)
    if not my_list:
        return 0
    else:
        return my_list[0] + my_sum(my_list[1:])


my_list = [1]
print("SUM:", my_sum(my_list))
my_list = [1, 2, 3, 4, 5]
print("SUM:", my_sum(my_list))


# Now the above function will work for numbers, will not work against strings.
# The below one will work for anything.
def my_sum_new(my_list):  # Here the parameter can take any type.
    return my_list[0] if len(my_list) == 1 else my_list[0] + my_sum_new(my_list[1:])


my_list = [1]
print("SUM:", my_sum_new(my_list))
my_list = [1, 2, 3, 4, 5]
print("SUM:", my_sum_new(my_list))
my_list = ['s', 'p', 'a', 'm']
print("SUM:", my_sum_new(my_list))
my_list = "spam"
# Here the string is actually getting converted to a list and again concatenated to the string.
print("SUM:", my_sum_new(my_list))
print()


# Functions: Attributes and Annotations.
# Indirect Function Calls.
def func(var):  # A basic simple function.
    my_str = "Hello World! "
    print(my_str * var)


func(8)
my_func_var = func  # Assigning the function object to a new variable - my_func_var
my_func_var(5)  # Calling the function using the new variable - my_func_var

print("Type of func:", type(func))  # Checking the type of the name 'func' which is the name of the function 'func'
print("Type of my_func_var:", type(my_func_var))  # Checking the type of the new variable 'my_func_var' - same.

# Checking the attributes of the function
print("Attributes", dir(func))
print("Attributes", dir(my_func_var))

# Checking few of the attributes
print("Name:", func.__name__)
print("Annotations:", func.__annotations__)
print("Class:", func.__class__)
print("Code:", func.__code__)
print("Defaults:", func.__defaults__)
print("Dict:", func.__dict__)
print("Dir:", func.__dir__)
print("Doc:", func.__doc__)


# A simple addition function
def addition(a, b, c):
    return a + + b + c


print(addition(1, 2, 3))


# Now attaching annotations to the same function as above, by just changing the name.
def new_addition(a: 'The first variable', b: 'The second variable', c: 'The third variable') -> int:
    return a + + b + c


print(new_addition(1, 2, 3))

# Here checking the attributes as above but this time with the 2 new annotations.
print("Attributes of addition() function:", dir(addition))
print("Annotations of function addition():", addition.__annotations__)

print("Attributes of new_addition() function:", dir(new_addition))
print("Annotations of function new_addition():", new_addition.__annotations__)
print()

# Anonymous Functions: lambda functions.
sum_of_values = lambda x, y, z: x + y + z
print("SUM:", sum_of_values(20, 30, 40))
print("FULL VALUE:", sum_of_values("I ", "get ", "it!"))

default_sum_of_values = lambda x=" NA ", y=" NA ", z=" NA ": x + y + z
print("FULL VALUE:", default_sum_of_values("I ", "get ", "it!"))
print("FULL VALUE:", default_sum_of_values("Apple"))

# map function: part of Functional Programming
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
inc_by_ten = list(map((lambda x: x + 10), list_of_numbers))
print(inc_by_ten)

str_list = ['a', 'b', 'c', 'd', 'e']
inc_str_list = list(map((lambda x: x * 5), str_list))  # Using lambda repeating the strings in a list
print(inc_str_list)
print()


def str_multiplication(numbers_list, str_list):
    final_list = []
    for number in numbers_list:
        final_list.append(list((value * number for value in str_list)))  # Using List Comprehension
    return final_list


str_multiplied_list = str_multiplication(list_of_numbers, str_list)
print(str_multiplied_list)
print()

# filter function: Another Functional Programming aspect.
list_of_numbers = list(range(1, 101))
print("Our Range:", list_of_numbers)
even_numbers = list(filter((lambda x: x % 2 == 0), list_of_numbers))
print(even_numbers)
odd_numbers = list(filter((lambda x: x % 2 != 0), list_of_numbers))
print(odd_numbers)
print()

# Using reduce to reduce the list to a single value.
from functools import reduce

sum_even_numbers = reduce((lambda x, y: x + y), even_numbers)
sum_odd_numbers = reduce((lambda x, y: x + y), odd_numbers)
print("Sum of Even Numbers:", sum_even_numbers)
print("Sum of Odd Numbers:", sum_odd_numbers)
