# Open for test output: create or empty.
myfile = open("my_data/myfile.txt", 'w') # Opens the connection of the text file for writing - w.
# Writing a string into the text file and returning the number of characters it has written.
print(myfile.write("Hello text file.\n"))
print(myfile.write("Goodbye text file.\n"))
myfile.close() # Closing the connection and flushing the buffer.

# Opens the connection of the text file for reading - r.
# Here the exact path is provided, hence raw string is used.
myfile = open(r"C:\Users\HP\Documents\GIT_REPOS\DataScience101\PyCharm_Projects\Python101\my_data\myfile.txt", 'r')
print(myfile.readline()) # Printing the first line from the file.
print(myfile.readline()) # Printing the second line from the file.
print()

# Reading the whole file at once.
first_file = open("my_data/first_file.txt") # Here the access specifier is not mentioned, cause read - r is the default.
print(first_file.read()) # Reading the whole file at once and printing it.
print()

# Reading the whole file using the file iterators.
for line in open("my_data/first_file.txt"):
    # The second parameter is to remove the '\n' at the end of the line as print statements already put a
    # new line ('\n') character at the end. So removed it with blank.
    print(line, end='')
print()
print()
print()

# Object serialization - Storing and parsing Python objects in a file.
X, Y, Z = 43, 44, 45
S = 'spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
F = open("my_data/second_file.txt", 'w')
F.write(S + '\n')
F.write('%s, %s, %s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()
F = open("my_data/second_file.txt")
print(F.read())

# Storing native Python objects with Pickle.
D = {'a': 1, 'b': 2}
F = open("my_data/datafile.pkl", 'wb')
import pickle
pickle.dump(D, F)
F.close()
F = open("my_data/datafile.pkl", 'rb')
E = pickle.load(F)
print(E)





