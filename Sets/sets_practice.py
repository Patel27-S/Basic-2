'''
For sets, there are methods to add elements :-
add(), update(), intersection_update,
symmetric_difference_update(), union_update() methods.

Methods to remove elements :-
remove(), discard(), pop() methods.
discard() method does not throw errors when to be discarded is not found.

Difference methods :-

difference() and symmetric_difference() methods.

'''

s1 = set([1,2,3,4,4])

# add() method :-

s1.add(5)

s2 = [9,10, 90]

# update() method :-

s1.update([6,7,8], s2)

s1.update([11,12,13,14,15])

print(s1)

# discard() method :-
s1.discard(45)

print(s1)

# remove() method :-

s1.remove(15)

print(s1)

# difference() method :- 

s3 = s1.difference(s2)

print(s3)

# symmetric_difference() method :-

s4 = s1.symmetric_difference(s2)

print(s4)


# union() method :-

s6 = {1,2,3,4}

s7 = {2,3,4,5}

s8 = s6.union(s7)

print(s8)

# intersection() method :-

s8 = s6.intersection(s7)

print(s8)

# issubset() method :-

s8 = s6.issubset(s7)

print(s8)
