'''
A Python program to check if a dictionary is empty. 
'''

# If the number of keys in a dictionary are zero,
# then we can say that a dictionary is empty.

# Logic used :- The number of keys in an empty dictionary are zero.
# Hence, we loop through the dictionary's keys and if the counter variable's
# value eventually comes out as zero, then the dictionary is empty.

def empty_dict(dictionary):
  '''
  This function checks if a dictionary 
  is empty.
  '''
  count = 0
  for keys in dictionary:
    count += 1
  if count == 0:
    return "The dictionary is Empty."
  else:
    return "The dictionary is NOT empty."

# Testing of the above function :

di = {}

print(empty_dict(di))