# User Inputs and While Loops.
# A Simple message printing.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello " + name + "!")
print()

# Using int() to accept numerical input.
age = input("How old are you? ")
print("Your age: " + age)
if int(age) >= 18:  # Converting the String value to the integer value using the int() function.
    print("You are an adult.")
else:
    print("You are not an adult.")
print()

# Introducing While Loops.
counter = 1
while counter <= 5:
    print("COUNT: " + counter.__str__())
    counter += 1
print()

# Infinite loop - the user choose when to quit.
message = ""
while message != 'quit':
    message = input("Enter your data: ")
    print(message)

# Another way of implementing the above using a flag.
message = ""
flag = True
while flag:
    message = input("Enter your data: ")
    if message == 'quit':
        flag = False
    else:
        print(message)
print()

# Another way of implementing the above using a break.
message = ""
while True:
    message = input("Enter your data: ")
    if message == 'quit':
        break
    else:
        print(message)
print()

# Using continue in a loop.
current_number = 0
list_of_even_num = []
while current_number <= 100:
    current_number += 1
    if current_number % 2 != 0:
        continue
    else:
        print("EVEN: " + current_number.__str__())
        list_of_even_num.append(current_number)
print(list_of_even_num)
print(len(list_of_even_num))
print()




