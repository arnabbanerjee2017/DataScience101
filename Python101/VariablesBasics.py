# This is a sample message stored in a variable.
message = "Hello Python World!"
print(message)

# This is a new sample message stored in the same variable as above, overriding the old value.
message = "Hello Python Crash Course World!"
print(message)

# String operations.
# Showing Quotes and Apostrophes in use. Look carefully.
print()
string1 = "This is a String."  # We can use Quotes to denote a String.
string2 = 'This is also a String.'  # We can use Apostrophes to denote a String.
string3 = 'I told my friend, "Python is my favorite language!"'  # We can use Quotes inside Apostrophes.
string4 = "The language 'Python' is named after Monty Python, not the snake."  # We can use Apostrophes inside Quotes.
string5 = "One of Python's strengths is its diverse and supportive community."  # We can use Apostrophes inside Quotes this way too.
print(string1)
print(string2)
print(string3)
print(string4)
print(string5)

# String Operations using in-built methods.
print()
name = "aRnAb BaNeRjEe"  # Here tha data contains both upper and lower case letters.
print(name.upper())  # To upper case letters.
print(name.lower())  # To lower case letters.
print(name.title())  # To print the first character of all the words in the text in upper case.

print()
firstName = "aRnAb"  # Here tha data contains both upper and lower case letters.
lastName = "BaNeRjEe"  # Here tha data contains both upper and lower case letters.
fullName = firstName + " " + lastName  # String concatenation
message = "Hello, Mr./Ms./Mrs. " + fullName.title() + "!"  # String concatenation
print(message)
print("Hello, Mr./Ms./Mrs. " + fullName.title() + "!")  # String concatenation

# Numerical Operations.
print()
print("NUMBERS")
print(2 + 3)  # Addition
print(3 - 2)  # Subtraction
print(2 * 3)  # Multiplication
print(3 / 2)  # Division
print(2 ** 10)  # Exponent/To-the-power
print(0.2 + 0.3)  # Floating point addition.
print(0.2 - 0.001)  # Floating point subtraction.
print(0.2 * 0.3)  # Floating point multiplication.
print(0.2 / 0.015)  # Floating point division.
print(0.2 + 0.1)  # Floating point addition. Check the result value.
print(3 * 0.1)  # Floating point multiplication. Check the result value.

# Integers with Strings
# Without the Integer to String conversion, this will throw error.
# Two ways to do that - using the str() method as shown below and __str__() on self method as shown below.
print()
age = 30
message = "Happy " + age.__str__() + "th birthday!!!"  # String concatenation with integer.
print(message)
message = "Happy " + str(age) + "th birthday!!!"  # String concatenation with integer.
print(message)

