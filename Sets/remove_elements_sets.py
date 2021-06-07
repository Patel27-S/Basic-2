#A Python program to remove all elements from a given set.

def remove_elements_set(set_1):
  set_2 = set()
  set_1.intersection_update(set_2)
  return set_1

# Testing of the above function :-

print(remove_elements_set({1,2,3,4}))
