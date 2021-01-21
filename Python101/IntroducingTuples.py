# Similar to Lists
# An immutable list is called a Tuple.

# Below is the same list as a Tuple.
cars = ('maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages')
print(cars)
print()

# Now different operations on it.
print(cars[0])  # Printing the first element in the Tuple.
print()

for car in cars:  # Looping through the Tuple.
    print(car.title())  # Printing each item in the Tuple with initial character in uppercase.

# Now trying to change a value.
# Changing a value
# The below statement will not execute, hence commented out. To check whether you can change a value in a Tuple,
# just remove the hashtag and run the program. You will get the error. This is because a Tuple is immutable, and once
# it is created, you cannot change the value.
# cars[-1] = 'ford'  # This will not work as a Tuple is immutable.
print(cars)



