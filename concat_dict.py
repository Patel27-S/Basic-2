'''
In this program, we have concatanated three 
dictionaries to form a new dictionary.
'''

# First of all we have three dictionaries.
# Hence, let us define three dictionaries :-

dict_1 = {"Smit" : "Maharaj"}
dict_2 = {"Maharaj" : "Guruji"}
dict_3 = {"Santo":"Haribhakto"}

# Let dict_4 be the dictionary that we want to store the
# resultant dictionary in.

dict_4 = dict()

# In the below loop, the itertating variable 'd' will iterate
# through each dictionary in the list, as the elements of the list 
# are dictionaries. And, in each iteration the 'dict_4' will be 
# updates/added with the respective value of 'd' which is nothing 
# but a dictionary element in the list.

for d in [dict_1, dict_2, dict_3]:
    dict_4.update(d)

print(dict_4)