'''
A program with a function that can add, multiply
and average out all the elements of a tuple.
'''

def tuple_elements_algebra(tuple):

    # For algebraic operations to happen, we need to make sure that all the elements are compatible :-
    for i in tuple:
        if  isinstance(i, int) == True or isinstance(i, float) == True:
            pass
        else:
            print('Sorry, Please make sure that all the values entered in tuple are either an integer or a float ;)')
            exit()

    # Addition of elements :-
    sum = 0
    for i in tuple:
        sum += i
    
    # Multiplication of elements :-
    mul = 1
    for i in tuple:
        mul *= i
    
    # Average of elements :-
    avg = sum / len(tuple)

    # Returning a tuple of sum, multiplication, average :-
    return (sum, mul, avg)


B = tuple_elements_algebra((23,34,45))
print(B)

A = tuple_elements_algebra(('a','b'))
print(A)
    





