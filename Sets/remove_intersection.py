def remove_intersection(set1, set2):
  '''
  Returns set1 which has empty intersection with set2.
  '''
  set3 = set1.intersection(set2)
  set1.difference_update(set3)
  return set1

# Testing of the above function :- 

set1 = {1,2,3}
set2 = {3,4,5}

print(remove_intersection(set1, set2))
