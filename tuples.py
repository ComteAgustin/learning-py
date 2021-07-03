# Tuples can't be modified and are more secure than lists
tuple = (1, 2, 3)
x = tuple((1, 2, 3)) # > (1, 2, 3)

singleTuple = (1)
print(singleTuple) # > class 'int'>

# del, delete all the tuple
del tuple # > error, tuple doesn't exist
