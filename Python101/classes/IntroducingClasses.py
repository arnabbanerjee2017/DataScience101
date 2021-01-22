# Introducing Classes and Object Oriented Programming.
class Dog():
    # A simple Dog class.
    def __init__(self, name, age):  # This is the init method or the constructor.
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " is rolled over.")

    def info(self):
        print("Dog's name: " + self.name.title() + " and Age: " + str(self.age))


my_dog = Dog('Brownie', 4)

my_dog.sit()
my_dog.roll_over()
my_dog.info()
