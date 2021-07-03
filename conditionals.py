# Conditionals
# Comparisons operators
3 > 2 # Greater-than

3 < 2 # less-than

3 == 3 # same-than

3 != 2 # not same-than

3 <= 2 # less and same-than

3 >= 5 # greater and same-than

# Logical operators
3>2 and 2>2 # if both conditions are true, return true
3>2 or 2>2 # need one of the conditions true, for return true
not(3>2) # the condition must be false, for return true

# if, do an action if the conditions is true
if 3 == 3: 
    print('is the same number')
elif 3 < 2 : # elif is an other condition
    print('not is the same, but yes is less')
else: # else is an action that be executed if the other conditions non be true
    print('not is the same number')

