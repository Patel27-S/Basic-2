'''
This Program checks if the given string is Even or Odd and 
accordingly returns the middle or the middle two characters 
in the respective cases.
'''

def str_ev_od(string):
    '''
    This function returns the middle character for Odd length 
    string and middle two characters for the Even length string.
    '''
    if len(string) %2 != 0:  # If the length of string is Odd.
        x = string[len(string)//2]
        return (x)           
    else:                    # If the length of string is Even.
        a = string[(len(string)//2)]
        b = string[((len(string)//2)-1)]
        return (a, b)        

print(str_ev_od('MS DHONI'))
