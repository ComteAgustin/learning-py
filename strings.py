myStr = "hello world"

# Functions
dir(myStr) # Return methods and properties, that i can use 

myStr.upper() # Return the string in uppercase
myStr.lower() # Return the string in lowercase
myStr.swapcase() # Convert the uppercase en lower case and the reverse
myStr.capitalize() # Convert the first letter in uppercase

# Count return the number of  
myStr.count('l') 
myStr.count('ll')

# StartWith, return if the string into the parameters start in the string
myStr.startswith('hello') # > true
myStr.startswith('bye') # > false

# Endswith, return if the string into the parameters finish in the string
myStr.endswith('world') # > true
myStr.endswith('carlos') # > false

# Replace any part of a string, for the string that i introduce in a parameters 
myStr.replace('hello', 'bye') # > "bye world"
myStr.replace('the string that i like replace', 'the string that i put')

# Spĺit, separate in string based in the char into the paramenters
myStr.split('') # > ["hello", "world"]

# Find, return the position of the first char into the parameter in the string
myStr.find('l') # > 2
myStr.find('w') # > 6

# Return true or false, depending if is a numeric data
myStr.isnumeric()
# Return true or false, depending if is a alpha numeric data
myStr.isalpha()