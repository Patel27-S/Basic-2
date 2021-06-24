def tuple_to_integer(tuple_1):
  '''
  This function converts a tuple of integer elements to
  a combined integer in the output. T.C. = O(n).
  '''
  string = ''
  for i in tuple_1:
    string += str(i)
  return int(string)

# Testing of the above function :-

print(tuple_to_integer((1,2,3)))