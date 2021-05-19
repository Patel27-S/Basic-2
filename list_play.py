'''This Python program will have a fucntion that accepts a list of numbers and 
   creates a list to store the count of negative number in first element and 
   store the sum of positive numbers in second element.'''

def detect_list(list_of_elements):
    '''
    This function detects the number of positive 
    and negative elements in list.
    '''
    count = 0    # Negative elements' counter tracker.
    count2 = 0    # Positive elements' counter tracker.

    for x in range(len(list_of_elements)):  
        if list_of_elements[x] < 0:        #  If the element is negative, counter variable is incremented.
            count = count + 1
        else:                              # If the element is positive, counter variable is incremented.
            count2 = count2 + 1
    
    print(str(count),' & ', str(count2), 'are the number of negative and positive elements in the list respectively.')



    






