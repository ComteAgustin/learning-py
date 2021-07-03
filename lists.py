# lists
demoList = ['carlos', 'juan', 'jose']

# With the method list, can i create a new list
colours = list(('red', 'brown', 'yellow'))

# value in list, return a boolean if the value is in the list 
'red' in colours # > true
'purple' in colours # > false

# Appends, add 1 element in the final of the list
colours.append('violet') # > ["red", "brown", "yellow", "violet"]

# Extend, add the element of the tuples/list how an elements in the list
colours.extend(('orange', 'green')) # > ["red", "brown", "yellow", "orange", "green"]

# Insert, add a new element in specific position
colours.insert(1, 'black') # > ["red", "black","brown", "yellow"]

# Pop, delete the last element or the index expressed in the list
colours.pop() # > ["red", "brown"]
colours.pop(1) # > ["red", "yellow"]

# Remove, delete a specific element
colours.remove('red') # > ["brown", "yellow"]

# Clear, remove all the elements
colours.clear() # > []

# Sort, sort all the elements in the list
colours.sort() # > ["brown", "red", "yellow"]
colours.sort(reverse=True) # > ["yellow", "red", "brown"]

# Index, get the index of the data in the parameters
colours.index('red') # > 0
colours.index('brown') # > 1
