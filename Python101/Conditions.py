# Checking if conditions.
# Same List object containing same items as previous examples.
cars = ['maruti suzuki', 'tata motors', 'suzuki', 'mahindra', 'hyundai', 'nissan', 'kia', 'morris garages']

# if-else statements inside a loop checking for equality.
for car in cars:
    if car.lower() == 'suzuki':
        print(car.upper())
    else:
        print(car.title())
print()

# if-else statements inside a loop checking for non-equality.
for car in cars:
    if car.lower() != 'suzuki':
        print(car.upper())
    else:
        print(car.title())
print()

# if statement to check a value present in a list.
if 'suzuki' in cars:
    print("Yes SUZUKI is present.")
print()

# if statement to check a value is not present in a list.
if 'tata' not in cars:
    print("Tata is not there but Tata Motors is there.")
print()

# if-elif-else statements demonstration.
age = 12  # Change the value according to the below conditions to test out the below code.
if age < 4:
    print("No need for admission charges.")
elif 4 <= age < 18:  # Here using the simplified version of the ((age >= 4) and (age < 18))
    print("You need to pay $5 for admission charges.")
else:
    print("You need to pay $10 for admission charges.")
print()

# Checking whether a List is empty or not.
empty_list = []
# If we pass the List name/ variable name, Python will check the List is having at least one item or not.
# If the list is having one item, Python return True, otherwise False.
if empty_list:
    print("The List is not empty.")
else:
    print("The List is empty.")
empty_list.append('Hello')
empty_list.append('World')
if empty_list:
    print("The List is not empty.")
else:
    print("The List is empty.")
print()
empty_list = []
# Here same case as above but we are using not here. Means if the list is empty it will evaluate to True in if.
if not empty_list:
    print("The List is empty.")
else:
    print("The List is not empty.")
empty_list.append('Hello')
empty_list.append('World')
if not empty_list:
    print("The List is empty.")
else:
    print("The List is not empty.")
print()

# Using Multiple Lists.
indian_cars = ['maruti suzuki', 'tata motors', 'mahindra', 'bajaj', 'honda', 'hyundai', 'toyota']
foreign_cars = ['maruti suzuki', 'hyundai', 'kia', 'ford', 'nissan', 'toyota', 'honda', 'yamaha', 'suzuki', 'volkswagen', 'mg']
for car in foreign_cars:
    if car in indian_cars:  # Checking a value is present in a List.
        print(car.upper() + " - the brand belongs to both India and to the world.")
print()
for car in indian_cars:
    if car in foreign_cars:  # Checking a value is present in a List.
        print(car.upper() + " - the brand belongs to both India and to the world.")
print()




