# python Data collection


- Lists
- Tuples
- Dictionaries
- Sets

## What are Data collections

# Lists
# Syntax ["London"]
# CRUD CREATE READ UPDATE DELETE

#WHAT ARE LISTS?
#LISTS ARE MUTABLE


shopping_list = ["juice", "strawberries", "yogurt", "chicken", "raspberries", "butter"]
              #      0           1             2          3            4           5
print(shopping_list)
print(type(shopping_list))

print(shopping_list[2])
print(shopping_list[4])
print(shopping_list[-1])

# if we needed to replace something from the list
shopping_list[5] = "oats"
print(shopping_list)

# if we needed to add something to a list we have a method called append
shopping_list. append("Mango")
print(shopping_list)

# if we want to remove something from a list we have a method called remove
shopping_list.remove("oats")
print(shopping_list)

# if we want to remove the last item from a list we use pop
shopping_list.pop()
print(shopping_list)

# Tuples are IMMUTABLE
# Syntax ()
# use cases

essentials = ("eggs", "milk", "bread")
              #   0       1        2
print(essentials)
print(type(essentials))

# replace bread with yogurt

essentials[2] = "yogurt"
print(essentials)

# what are dictionaries?
# are structured as KEY = VALUE
# VALUE could be string, int, list
# Syntax {}

student_1 = {
    "name": "Munira",
    "key": "value",
    "stream": "Cyber Security", # string
    "completed_lessons": 3, # int
    "complete_lessons_names": ["variables", "operators", "data_collections"]

}
print(student_1)
print(student_1["name"])
print(student_1["stream"])
print(student_1["complete_lessons_names"])
# display only OPERATORS FROM THE LIST INSIDE DICTIONARY -
print(student_1.keys())
print(student_1.values())


#what are dictionaries?  
#are structured as KEY = 
#VALUE could be string, i
#Syntax {}               
                         
# student_1 = {
#     "name": "Munira",
#     "key": "value",
#     "stream": "Cyber Security", # string
#     "completed_lessons": 3, # int
#     "complete_lessons_names": ["variables", "operators", "data_collections"]
}                        
                         
# print(student_1)
# print(student_1["name"])
# print(student_1["stream"])
# print(student_1["complete_lessons_names"])
# print(student_1["complete_lessons_names"][1]) # Name of the dictionaries followed by the key then then index of the value you want to retrieve
# # display only OPERATORS FROM THE LIST INSIDE DICTIONARY -
# print(student_1.keys())
# print(student_1.values())

# Sets are data collection but the difference is that they are unordered
#Syntax name = {}

car_parts = {"wheels", "doors", "engine"}
print(car_parts)

# Can we add any new parts?
car_parts. add("windows")
print(car_parts)

# Can we remove an item
car_parts.discard("doors")
print(car_parts)

# Frozen sets they are like Tuples
frozen_set = ([1,3,5,6])
print(frozen_set)


                         
                         
