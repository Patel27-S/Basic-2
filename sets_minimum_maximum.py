'''
A program with functions to find maximum and minimum value from a set.
'''

set_1 = set([-1,-2,3,4,5,6,7])

# A function which returns the maximum element upon passing the set.

def maximum_element_set(set_ji):   # same as maximum_set()
  return max(set_ji)

# A function which returns the minimum element upon passing the set.

def minimum_element_set(set_ji): # same as minimum_set()
  return min(set_ji)

def maximum_set(set_ji):
  largest = 0
  for i in set_ji:
    if largest> i:
      pass
    else:
      largest = i
  return largest


def minimum_set(set_ji):
  smallest = 0
  for i in set_ji:
    if smallest < i:
      pass
    else:
      smallest = i
  return smallest


# Testing of the above functions :-
    
print(maximum_set(set_1))
print(maximum_element_set(set_1))

print(minimum_set(set_1))
print(minimum_element_set(set_1))