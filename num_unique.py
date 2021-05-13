'''The program will determine whether an input of sequence 
    of numbers are all unique or not.
    '''

def find_uniqueness(List):
    '''This function finds if the elements
        are unique in the List.
        '''
    if len(List) == len(set(List)):  #  Set doesn't have duplicates.
        return True
    else:
        return False


# The Time Complexity of the below function is O(n^2).

def find_uniqueness2(List):
    '''This function determines the uniqueness
        of elements in the List.
        '''
    for i in range(0, len(List)-1):  
        for j in range(i+1, len(List)):
            if List[i] == List[j]:  # Equal value condition while comparing
                return False
    return True

