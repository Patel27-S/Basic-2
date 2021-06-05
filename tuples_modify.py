'''
A  Python program to remove an item from a tuple.
'''

# Since tuples are immutable we cannot directly delete an element from a tuple.
# We need to convert it into a list in order to modify it and then we can convert it to a tuple.

def tuple_modify(tuple_1):
  '''
  This functions returns a modified/one-element removed
  version of the argument tuple.
  '''
  list_1 = list(tuple_1)
  list_1.pop()
  tuple_1 = tuple(list_1)
  return tuple_1
  
# Testing of the above function :-

T = tuple_modify((1,2,3,4))
print(T)
