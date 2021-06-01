  
'''
A program to count the number of elements until 
we encounter a tuple as an element in a list.
'''

def count_until_tuple(list):
    '''
    This function returns the number of elements until a tuple 
    is found in the list.
    '''
    counter = 0
    
    for i in list:
        if isinstance(i, tuple):
            break
        else:
            counter += 1
    return counter


# Testing of the above function :-

list = [1,2,3,"Smit", "Mihirbhai", (1,2,3), 78]

a = count_until_tuple(list)
print(a)
