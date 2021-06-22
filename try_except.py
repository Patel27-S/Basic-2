'''
This program is so that I can brush up the 
try-except concept in Python.
'''

try:
  a = float(input('Please enter numerator : '))
  b = float(input('Please enter denomiator : '))
  print(a/b)
except ZeroDivisionError as e:
  print('Please do not put zero as a denominator for division.')
except ValueError as e:
  print('Please enter a valid entry(i.e. such as a float value.)')
except Exception as e:
  print('Sorry, There is an error!', e)
finally:
    print('I enjoyed learning try-except handling in Python.')
