'''
This program has a function which returns the oldest student of the given students' 
name and age pairs in the form of dictionary.
'''


def oldest_stu(dictionary):
    '''
    Returns the oldest student when a dictionary of 
    students and their age value pairs are input.
    '''
    largest = -1
    oldest_std = None
    for student,age in dictionary.items():  # This will iterate through all the student,age pairs in the dictionary.
        if age > largest:
            largest = age
            oldest_std = student
    return oldest_std, largest

