# Passing an arbitrary number of arguments with a positional argument.
def make_pizza(size, *toppings):
    print("Size: " + size.__str__())
    print("Toppings:")
    for val in toppings:
        print(val.title())


