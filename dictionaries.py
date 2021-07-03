# Dictionaries 
book = {
   "name": 'book',
   "price": 3.99,
   "quantity": 4
}

person = {
    "first_name": 'Agustin',
    "last_name": 'Comte'
}

# Dictionaries can be almacened into a list
product = [ 
    {
        "name": 'book',
        "pric": 3.99,
        "quantity": 4
    },
    {
        "first_name": 'Agustin',
        "last_name": 'Comte'
    }
]

# keys, return all the keys
person.keys() # > [("first_name", "last_name")]

# items, return all the dictionary
person.items() # > [("first_name", "Agustin"), ("last_name", "Comte")]
 
# clear, delete all the element in the dictionary
person.clear()

# del, delete the dictionary
del person