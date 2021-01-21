# A sample List containing few bicycles.
# List starts with '[' and ends with ']', separated by commas.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # Printing the whole List.
print(bicycles[0])  # Printing the 1st elements of the List.
print(bicycles[1].title())  # Printing the 1st elements of the List with first letter in upper case.
print()

# Indexing in a List.
print(bicycles[1])  # Refers to the 2nd element of the List.
print(bicycles[-1])  # -1 refers to the last element of the List.
print(bicycles[-2])  # -2 refers to the 2nd last element of the List.
print()

# Individual values from a List.
message = "My first bicycle was a " + bicycles[0].title() + '!'  # concatenating a List value with Strings.
print(message)
print()

# Modifying elements in a List.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[0])
motorcycles[0] = 'ducati'  # Modifying the first element of the List.
print(motorcycles)
print(motorcycles[0])
print()

# Adding elements to a List.
# Appending elements.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  # Appending a value to the List.
print(motorcycles)
# Creating an empty List and then add all the items individually.
motorcycles = []  # Empty List.
print(motorcycles)
motorcycles.append('honda')  # Appending the value.
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
# Inserting elements into a List.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')  # inserting a value at the specified location in the List.
print(motorcycles)
print()

# Deleting an item from the List
del motorcycles[0]  # Deleting an element from the List using the del statement.
print(motorcycles)
motorcycles.__delitem__(1)  # Deleting an element from the List using the __delitem__() method of the List object.
print(motorcycles)
print()

# Pop an item from the List like a stack.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycle = motorcycles.pop()  # Pop the last elements of the List and store it to the variable.
print(motorcycles)
print(motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycle = motorcycles.pop(1)  # Pop the specified elements of the List and store it to the variable.
print(motorcycles)
print(motorcycle)
print()

# Removing an item by value.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')  # Removing an element from the List by value.
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'honda'
motorcycles.remove(too_expensive)  # Removing an element from the List by value stored in a variable.
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me!!!")  # Concatenation.
print()

# Sorting a List permanently with the sort() method.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
print(cars)
cars.sort()  # Permanent sorting.
print(cars)
cars.sort(reverse=True)  # Permanent reverse sorting.
print(cars)
print()

# Sorting a List temporarily with the sorted() function.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
print("Here is the original List: " + cars.__str__())
print("Here is the temporarily sorted list: " + sorted(cars).__str__())  # Temporary sorting.
print("Here is the original List again which is not sorted: " + cars.__str__())
print()

# Print a List in reverse order.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
print(cars)
cars.reverse()  # reverse() method on the List object.
print(cars)
print()

# Finding the length of a List.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
print(cars)
print(len(cars))  # len() function to check the length of the List.
print()

# Looping through a List - for loop.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
print("The name of the Car Manufacturers: ")
counter = 1
for car in cars:  # This is called for loop or for-each loop.
    print(car.title() + " is checked!!!")
    print("Counter: " + counter.__str__())
    counter += 1
print()

# Making Numerical Lists.
# Using the range() Function.
print("NUMERICAL LISTS")
nums = range(1, 21)
print(nums)
for num in nums:
    print("Values: " + num.__str__())
print()
for num in range(1, 21):
    print("Values directly from range(1, 21): " + num.__str__())
print()

# Using range() to make a List of Numbers.
nums = list(range(1, 21))
print(nums)
for num in nums:
    print("Values directly from a List generated from a range: " + num.__str__())
print()
even_numbers = list(range(2, 21, 2))  # here the range() is range(starting_value, target_value, increment).
print(even_numbers)
print()
squares = []
for num in range(1, 11):
    squares.append(num ** 2)  # To get the square of each number and appending to the squares list created above.
for num in squares:
    print("Square Result: " + num.__str__())
print()

# Simple Statistics with a List of Numbers.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min_num = min(digits)  # Get the minimum value from a List.
max_num = max(digits)  # Get the maximum value from a List.
sum_num = sum(digits)  # Get the sum of all the items in a List.
avg_num = sum_num / len(digits)  # Get the average value from a List. Right now doing it manually.
print("Max Num: " + max_num.__str__())
print("Min Num: " + min_num.__str__())
print("Sum Num: " + sum_num.__str__())
print("Avg Num: " + avg_num.__str__())
print()

# List Comprehension.
# A List Comprehension allows you to generate the same list in just one line of code.
# Same example to get the square of each number in a List as above.
squares = [value ** 2 for value in range(1, 11)]  # This is List Comprehension.
print(squares)
print()

# Working with Part of a List.
# Slicing a List.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
print(cars[0:3])
print(cars[1:5])
print(cars[2:])
print(cars[:6])
print(cars[-4:])
print(cars[:-4])
print()

# Looping through a Slice.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
for car in cars[1:6]:
    print("Selected Brand: " + car.title())
    for alphabet in car.title():
        print("Alphabet: " + alphabet)
    print()
print()

# Copying a List
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
cars_duplicated = cars  # This is just referring to the same List object. Think of a pointer.
print("cars: " + cars.__str__())  # Both are same Lists
print("cars_duplicated: " + cars_duplicated.__str__())  # Both are same Lists
# Trying modify a cars list.
cars.append('ford')  # This will affect the both the lists as this is basically a single list pointed by 2 variables.
print("After appending new brand to the cars list.")
print("cars: " + cars.__str__())  # This will show the appended value.
print("cars_duplicated: " + cars_duplicated.__str__())  # This will show the appended value too.
print()
# Now actual copying.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']
# This slicing the actual list from 0 to the end as no number is specified.
# And creating a copy of that sliced list and assigns it to the variable. So here 2 separate lists are present
# having same values till now.
cars_duplicated = cars[:]
print("cars: " + cars.__str__())  # Different list with same values.
print("cars_duplicated: " + cars_duplicated.__str__())  # Different list with same values.
# Trying modify a cars list.
cars.append('ford')  # This will affect only the cars list.
print("After appending new brand to the cars list.")
print("cars: " + cars.__str__())  # This will show the appended value as it is separate list now.
print("cars_duplicated: " + cars_duplicated.__str__())  # This contains the old values without the new appended value.



