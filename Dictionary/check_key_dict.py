'''
Here we have a program, already having a dictionary.
We have to check if it contains a specific key.
'''


# The below function takes two parameters :
# A Dictionary and a Key.
# It checks whether the input Dictionary has the Key to
# be searched or not.

def check_key_dict(dic, key):
    '''
    The function returns 'True' if the key is found
    in the dictionary or 'False' otherwise.
    '''
    for key_1 in dic:
      if key_1 == key:
          return True
    return False

# Time Complexity of the above function is O(n) as
# it will run until the element is found; at maximum until
# the last key of the dictionary.

# Testing of the function :-

dictionary = {
  'Smit' : 'Maharaj',
  'Maharaj' : 'Guruji',
  'Guruji' : 'Santo',
  'Santo' : 'Haribhakto'
}

result = check_key_dict(dictionary, 'Smit')
print(result)
