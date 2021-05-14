'''
This program will help knowing the frequency of
each word and also the most common word in the file,
that we enter.
'''
prompt_string = input("Enter a file name : ")  # Prompts the user to enter the file name.
fhandle = open(prompt_string,'r')  # The entered string is opened as a file.

count = dict() 

for line in fhandle:    # This loop will run through all the lines of the file.
    words_list = line.split()
    for word in words_list:    # This loop will run through each word in a line's list.
        count[word] = count.get(word,0) + 1    # New count = Old count + 1 or 1(If a newly found word).


largest = 0  
common_word = None
for key,value in count.items():    # This loop iterates through all the key, value pairs of dictionary.
    if value > largest:
        largest = value
        common_word = key
        

print(largest, "is the frequency of the most common word : ",common_word, '.')