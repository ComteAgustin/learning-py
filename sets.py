# Sets are a collection without index
colours = {'red', 'green', 'black'}

# value in set, return true or false
'red' in colours # > true
'white' in colours # > false

# add, add a new element at the set start 
colours.add('white') # > {"white", "red", "green", "black"}

# remove, remove a element
colours.remove('black') # > {"red", "green"}

# clear, reset all the set
colours.clear() # > set()

# del, delete all the set
del colours