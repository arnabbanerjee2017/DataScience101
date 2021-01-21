# Advanced Function Concepts.

# Recursion.
def my_sum(my_list):  # The paramter will only take numbers otherwise raise exception.
    print(my_list)
    if not my_list:
        return 0
    else:
        return my_list[0] + my_sum(my_list[1:])


my_list = [1]
print("SUM:", my_sum(my_list))
my_list = [1, 2, 3, 4, 5]
print("SUM:", my_sum(my_list))


# Now the above function will work for numbers, will not work against strings.
# The below one will work for anything.
def my_sum_new(my_list):  # Here the parameter can take any type.
    return my_list[0] if len(my_list) == 1 else my_list[0] + my_sum_new(my_list[1:])


my_list = [1]
print("SUM:", my_sum_new(my_list))
my_list = [1, 2, 3, 4, 5]
print("SUM:", my_sum_new(my_list))
my_list = ['s', 'p', 'a', 'm']
print("SUM:", my_sum_new(my_list))
my_list = "spam"
# Here the string is actually getting converted to a list and again concatenated to the string.
print("SUM:", my_sum_new(my_list))