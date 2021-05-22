'''
A Python script to check whether a 
given key already exists in a dictionary or not.
'''


def key_presence(dic, key):
  '''
  This function returns the attendance 
  of the key in a given dictionary.
  '''
  if key in dic:  
    return "{} is present in the dictionary.".format(key)
  else:
    return "{} is not present in the dictionary.".format(key)
    

    
# Practice testing of the function is below :-

dict_1 = {"Smit": "Guruji", "Guruji": "Santo", "Maharaj": "Santo"}

practice_1 = key_presence(dict_1,"Smit")

practice_2 = key_presence(dict_1, "MSDHONI")

print(practice_1)

print(practice_2)
