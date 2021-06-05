'''
Here we have a program, already having a dictionary.
We have to check if it contains a specific key.
'''


# The below function takes two parameters :
# A Dictionary and a Key.
# It checks whether the input Dictionary has the Key to 
# be searched or not.

def check_key_dict(dic, key):
  for keys in dic:
    if keys == key:
      return True
  return False
  
  

# Testing of the function :- 

dictionary = {
  'Smit' : 'Maharaj',
  'Maharaj' : 'Guruji',
  'Guruji' : 'Santo',
  'Santo' : 'Haribhakto'
}
  
result = check_key_dict(dictionary, 'Smit')
print(result)