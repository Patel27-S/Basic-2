'''
Note :- In this program, I haven't used any of python's inbuilt
libraries or functions' help
All that was needed, has been coded by myself.
 '''


def largest(required, *args):
  if len(args) == 2:
    largest = None
    if required > args[0]:
      if required > args[1]:
        largest = required
    elif args[0] > args[1]:
      largest = args[0]
    else:
      largest = args[1]
    return largest
  elif len(args) == 1:
    if required > args[0]:
      largest = required
    else:
      largest = args[0]
    return largest 



 

list = [('Smit', 1.3),('Mihirbhai', 3.4),('Sahilbhai',3.9)]



l = largest(list[0][1], list[1][1], list[2][1])

if list[2][1] is l:
  dummy = list[0]
  list[0] = list[2]

  m = largest(dummy[1], list[1][1])

  if dummy[1] is m:  
    dummy_2 = list[1]
    list[1] = dummy
    list[2] = dummy_2
  else:
    list[2] = dummy

elif list[1][1] is l:
  dummy = list[0]
  list[0] = list[1]
  n = largest(dummy[1],list[2][1])
  
  if dummy[1] is n:
    dummy_2 = list[1]
    list[1] = dummy
    
elif list[0][1] is l:
  # Here list[0] is at the right position
  o = largest(list[1][1], list[2][1])

  if list[1][1] is o:

    pass
  elif list[2][1] is o:
    list[1], list[2] = list[2], list[1]


print(list)