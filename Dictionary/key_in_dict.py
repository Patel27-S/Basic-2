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


def key_in_dict_1(dict, find_key):
    for any_key in dict:
        if any_key == find_key:
            return True
    return False

# Both of the above functions are O(n) or Linear Time Procedures
# performing the same task.

# Testing of the functions is below :-

dict_1 = {"Smit": "Guruji", "Guruji": "Santo", "Maharaj": "Santo"}

practice_1 = key_presence(dict_1,"Smit")

practice_2 = key_in_dict_1(dict_1,"Smit")

practice_3 = key_presence(dict_1, "MSDHONI")

practice_4 = key_in_dict_1(dict_1, "MSDHONI")

print(practice_1)

print(practice_2)

print(practice_3)

print(practice_4)
