# Iterations and Comprehensions.
L = [1, 2, 3]  # A sample list containing some values.

# Internally the for loop calls the iter() function, passes the list object and obtains the iterator object.
for item in L:  # Iterating through the list. The for loop causes attaching the iterator automatically.
    print("Value:", item)
print()

iterator_l = iter(L)  # Manually taking an iterator over the list object.
# Using the default built-in __next__() function to fetch the current value and point to the next value.
print("Value:", iterator_l.__next__())
print("Value:", next(iterator_l))  # Using the next() function which internally calls the __next__() function.
print("Value:", iterator_l.__next__())
print()

D = {'a': 1, 'b': 2, 'c': 3}  # A sample dictionary object containing some values.
keys = iter(D)  # Getting an iterator object of keys by passing the dictionary to the iter function manually.
print("KEY:", keys.__next__())  # Calling the __next__() function.
print("KEY:", keys.__next__())
print("KEY:", keys.__next__())
print()

for key in D:  # Automatically calls the iter function, passes the dictionary object, and obtain an iterator of keys.
    print("KEY:", key)
print()

# List Comprehension.
new_list = [i + 1 for i in range(100)]  # Creating a list of 100 values from a range using List Comprehension.
print(new_list)
new_list = [i + 10 for i in new_list]  # Adding 10 to each member of the list using List Comprehension.
print(new_list)
# Creating two lists, one for even and other is for two, using List Comprehension.
even_list, odd_list = [i + 10 for i in new_list if i % 2 == 0], [i + 10 for i in new_list if i % 2 != 0]
print(even_list)
print(odd_list)
print("Length of new_list:", len(new_list))
print("Length of even_list:", len(even_list))
print("Length of odd_list:", len(odd_list))


