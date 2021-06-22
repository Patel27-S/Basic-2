'''
Given the centre co-ordinates and radius values
of two circles, the below program will determine if 
they're intersecting.
''' 

x1 = float(input("Please Enter the x-coordinate of the center of circle : "))
y1 = float(input("Please Enter the y-coordinate of the center of circle : "))
r1 = float(input("Please Enter the radius of the circle  : "))

x2 = float(input("Please Enter the x-coordinate of the center of another circle : "))
y2 = float(input("Please Enter the y-coordinate of the center of another circle : "))
r2 = float(input("Please Enter the radius of another circle  : "))

distance_centres = ((x1-x2)**0.5 + (y1-y2)**0.5)**0.5   # If the distance between centres of circle is radius than the sum of their
                                                        # radius values implies that the circles are intersecting with each other.

if distance_centres <= r1+r2:
  print("Both the circles are intersecting.")
  
