'''
A Python script to print a dictionary where the keys 
are numbers between 1 and 15 (both included) and the values 
are square of keys
'''
# Here, we have defined a dictionary first.
d = dict()

'''
The statement below will prompt the user to enter an integer
which will be equal to the number of elements in the output dictionary.
And, also would the number until which the number:number^2 pairs would be generated
and added/updated to the dictionary.
'''
n = int(input('Please enter an integral number you want '\
             'the number:number*number pattern until in'\
             ' a dictionary : '))


for i in range(1,n+1):
  d.update({str(i): i*i}) # 'str()' used so that keys and values are identifiable distinctly.

print(d)
