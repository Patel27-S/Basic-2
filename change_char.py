"""
This program contains a function that chnages 
all the characters in a string following the first 
character euqal to '$', if found equal to the first 
character.
"""

def change_char(string):
  '''This function changes all the 
  first character re-occurences to '$' sign
  in the input string.'''
  a = string[0] 
  output_string = ''
  
  # The loop iterates through all the indices of string.
  
  for i in range(len(string)):
    
    # If the character is not same as 1st character
    # Simple concatenation with the same character
    if i == 0 or string[i] != a:
      output_string += string[i]
      
    # If the character is equal to 1st character.
    else: 
      output_string += '$'
      
  return output_string
  
  # Note :- The above function is case-sensitive.
