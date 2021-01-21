# A Dictionary in Python is similar to a Map in Java or a JSON.
# This is the first Dictionary.
# A Dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key
# to access the value associated with that key.
# Here the Dictionary contains some details about a specific car.
first_car = {'brand': 'maruti suzuki', 'model': 'S-Presso', 'variant': 'vxi+', 'color': 'sparkling blue'}
print(first_car)
print(first_car['brand'].title())
print(first_car['model'])
print(first_car['variant'].upper())
print(first_car['color'].title())
print()

# Adding new key-value pairs in the Dictionary.
first_car['price'] = 500000
first_car['rto'] = 'barasat, wb, india'
first_car['city_of_purchase'] = 'kolkata'
first_car['current_location'] = 'south dum dum, north 24 parganas, wb, india'
print(first_car)
print()

# An empty Dictionary.
second_car = {}
second_car['brand'] = 'maruti suzuki'
second_car['model'] = 'Ertiga'
second_car['variant'] = 'vxi'
second_car['color'] = 'grey'
print(second_car)
print()

# Modifying a Dictionary.
second_car['color'] = 'dark blue'
print(second_car)
print()

# Deleting an key-value pair from a Dictionary.
print(first_car)
del first_car['price']
print(first_car)
print()

# Looping through a Dictionary.
# Looping through all Key-Value Pairs.
for key, value in first_car.items():
    if key.lower() == 'variant':
        print("Key: " + key.upper() + ", Value: " + value.upper())
    elif value.lower().__contains__('wb'):
        print("Key: " + key.upper() + ", Value: " + value.upper())
    else:
        print("Key: " + key.upper() + ", Value: " + value.title())
print()

# Looping through all the keys in a Dictionary.
# In below statement, the keys() method on the Dictionary is optional. It can be ignored as if nothing is provided,
# it is implicit that the keys will be picked up by Python automatically.
for key in first_car.keys():
    if key.lower() == 'variant':
        print("Key: " + key.upper() + ", Value: " + first_car[key].upper())
    elif first_car[key].lower().__contains__('wb'):
        print("Key: " + key.upper() + ", Value: " + first_car[key].upper())
    else:
        print("Key: " + key.upper() + ", Value: " + first_car[key].title())
print()

# Looping through a Dictionary's Keys in order.
for key in sorted(first_car.keys()):
    if key.lower() == 'variant':
        print("Key: " + key.upper() + ", Value: " + first_car[key].upper())
    elif first_car[key].lower().__contains__('wb'):
        print("Key: " + key.upper() + ", Value: " + first_car[key].upper())
    else:
        print("Key: " + key.upper() + ", Value: " + first_car[key].title())
print()

# Looping through all the values in a Dictionary.
for value in first_car.values():
    print("Value: " + value.upper())
print()

# Nesting
# A List of Dictionaries.
first_car = {'brand': 'maruti suzuki', 'model': 'S-Presso', 'variant': 'vxi+', 'color': 'sparkling blue'}
second_car = {'brand': 'maruti suzuki', 'model': 'Ertiga', 'variant': 'vxi', 'color': 'grey'}
third_car = {'brand': 'maruti suzuki', 'model': 'breza', 'variant': 'vxi', 'color': 'red'}
cars = [first_car, second_car, third_car]
print(cars)
for car in cars:
    print(car)
print()

# A Dictionary of Lists.
brands = ['maruti suzuki', 'tata motors', 'hyundai', 'mahindra']
car_models = ['S-Presso', 'Ertiga', 'Swift', 'Dzire', 'Tiago', 'Tigor', 'Nexon', 'Harrier', 'i10', 'i20', 'Santro',
              'Scorpio', 'Bolero', 'XUV300', 'TUV300']
car_brand_and_model_mix = {'brands': brands, 'models': car_models}
print(car_brand_and_model_mix)
for each_car in car_brand_and_model_mix.values():
    print(each_car)
print()

# A Dictionary in a Dictionary.
all_cars = {'first_car': first_car, 'second_car': second_car, 'third_car': third_car,
            'car_brand_and_model_mix': car_brand_and_model_mix}
print(all_cars)
for key in all_cars:
    print("Key: " + key + "\tValue:" + all_cars[key].__str__())
print()






