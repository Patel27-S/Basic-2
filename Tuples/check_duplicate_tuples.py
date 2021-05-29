''' 
A Python program to find the repeated items of a tuple.
'''


def check_duplicate(tuple_1):
    '''
    This function checks if a tuple has duplicate
    values in it.
    '''
    set_1 = set(tuple_1)
    if len(set_1) == len(tuple_1):
      return "There are no duplicates in the tuple."
    else:
      return "There are duplicates in the tuple."


# Testing of the function :-

result = check_duplicate((1,2,3,4))

print(result)
