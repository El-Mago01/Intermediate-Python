import math

def get_max(list_of_numbers):
    return max(list_of_numbers)

def only_unique(list_of_numbers):
    my_set = set(list_of_numbers)
    my_new_list=list(my_set)
    return my_new_list

def starts_with(my_string, start_string):
    return  start_string in my_string[0:]

def factorial(number):
    return math.factorial(number)

def all_equal(my_list):
    return len(set(my_list)) == 1

