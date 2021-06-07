# A Python program to check if two given sets have no elements in common.

def check_empty_intersection(set_1, set_2):
  '''
  This function returns 'True' if intersection result is an empty set or 'False' otherwise.'''
  if set_1.intersection(set_2) == set():
    return True
  else:
    return False

# Testing of the above function :-

print(check_empty_intersection({1,2}, {1,4})) # returns 'False'.

print(check_empty_intersection({1,2}, {3,4})) # returns 'True'.
