import IntroducingModulesWithFunctions as mod


# Defining a Function.
def greet_user():
    print("Hello!")


greet_user()


# Passing information to a Function.
def greet_user(username):
    print("Hello " + username + "!")


greet_user("Arnab")
print()


# Positional Arguments.
def describe_pet(pet_type, pet_name='sunny'):  # With default value of a parameter. The parameter is allowed.
    print("I have a " + pet_type + ".")
    print("My " + pet_type + "'s name is " + pet_name.title() + ".")
    print()


describe_pet("cat", "hulo")
describe_pet("dog", "bhulu")
describe_pet(pet_type='horse', pet_name='hosy')  # Keyword Arguments.
describe_pet(pet_name='bhalu', pet_type='bear')  # Keyword Arguments.
describe_pet("dog")  # Will use the default value in place of pet_name as only pet_type is supplied.
describe_pet(pet_type="dog")  # Again using the default value here with the Keyword Arguments.


# Again positional arguments with both the default values. This is much flexible if it is allowed.
def describe_pet(pet_type='dog', pet_name='sunny'):  # With default values of both parameters.
    print("I have a " + pet_type + ".")
    print("My " + pet_type + "'s name is " + pet_name.title() + ".")
    print()


describe_pet("cat", "hulo")
describe_pet("dog", "bhulu")
describe_pet(pet_type='horse', pet_name='hosy')  # Keyword Arguments.
describe_pet(pet_name='bhalu', pet_type='bear')  # Keyword Arguments.
describe_pet("cat")  # Will use the default value in place of pet_name as only pet_type is supplied.
describe_pet(pet_type="cat")  # Again using the default value here with the Keyword Arguments.
describe_pet()  # Passing nothing will cause the use of both the default values.

print("=======================================================================")


# Return Values using the same example as above.
def describe_pet(pet_type='dog', pet_name='sunny'):  # With default values of both parameters.
    value_str = "I have a " + pet_type + "." + "\nMy " + pet_type + "'s name is " + pet_name.title() + ".\n"
    return value_str  # Returning the above created string.


returned_value = describe_pet("cat", "hulo")  # Calling the function and storing the returned value in the variable.
print(returned_value)
returned_value = describe_pet("dog", "bhulu")
print(returned_value)
returned_value = describe_pet(pet_type='horse', pet_name='hosy')  # Keyword Arguments.
print(returned_value)
returned_value = describe_pet(pet_name='bhalu', pet_type='bear')  # Keyword Arguments.
print(returned_value)
returned_value = describe_pet("cat")  # Will use the default value in place of pet_name as only pet_type is supplied.
print(returned_value)
returned_value = describe_pet(pet_type="cat")  # Again using the default value here with the Keyword Arguments.
print(returned_value)
returned_value = describe_pet()  # Passing nothing will cause the use of both the default values.
print(returned_value)

print("=======================================================================")


# Return Values using the same example as above. A more simpler form - the way programmers' use it.
def describe_pet(pet_type='dog', pet_name='sunny'):  # With default values of both parameters.
    return "I have a " + pet_type + "." + "\nMy " + pet_type + "'s name is " + pet_name.title() + ".\n"


print(describe_pet("cat", "hulo"))  # Calling the function and storing the returned value in the variable.
print(describe_pet("dog", "bhulu"))
print(describe_pet(pet_type='horse', pet_name='hosy'))  # Keyword Arguments.
print(describe_pet(pet_name='bhalu', pet_type='bear'))  # Keyword Arguments.
print(describe_pet("cat"))  # Will use the default value in place of pet_name as only pet_type is supplied.
print(describe_pet(pet_type="cat"))  # Again using the default value here with the Keyword Arguments.
print(describe_pet())  # Passing nothing will cause the use of both the default values.

mod.make_pizza(12, "onion")
print()
mod.make_pizza(14, "onion", "chicken", "Cheese", "tomato")

# Arbitrary Arguments Example.
print("=====================================================================================")
print("Arbitrary Arguments Example.")


# Collecting Arguments.
def func(*args): print(type(args), args); return args  # Printing the type of the argument passed, as told, it is tuple.


func(1)  # Passing just one simple argument.
func(1, 2, 3, 4)  # Passing 4 arguments.
for i in func(1, 2, 3, 4):  # Parsing the return value - tuple in a for loop.
    print(i * i)  # Printing the square of each number.


# This function takes a simple positional argument, a positional tuple, and a keyword dictionary.
def func2(a, *pargs, **kargs):
    print(type(a), a, type(pargs), pargs, type(kargs), kargs)  # Checking as usual.


func2(1, 2, 3, x=1, y=2)  # Calling the function as required - value, list of values, and keyword arguments.


# Unpacking Arguments.
def func3(a, b, c, d):  # The tuple is unpacked here.
    print("Unpacking Arguments: ", type(a), type(b), type(c), type(d), a, b, c, d)


args = (1, 2)
args += (3, 4)
func3(*args)  # The tuple is unpacked.
d = {'a': 5, 'b': 6, 'c': 7}
d['d'] = 8

func3(**d)



