'''
A program to convert a given string to a tuple.
'''

def string_to_tuple(string):
    '''
    A function to convert a given string to a tuple.
    '''
    list1 = list() # Declared a list.

    for i in string:
        list1.append(i)  # Converted a string to a list.
    return tuple(list1) # returned a tuple version of the formed list.


# Note :- Here we cannot directly convert a string to a tuple, because tuples are immutable(so can't be appended).
# Hence, we have to convert the string first into a list and then a list into a tuple.

# Testing of the above function :-

output_tuple = string_to_tuple('Shreeji-Guruji-Santo-Bhakto')

print(output_tuple)
