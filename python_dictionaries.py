# #what are dictionaries?
# #are structured as KEY = VALUE
# #VALUE could be string, int, list
# #Syntax {}
#
# student_1 = {
#     "name": "Munira",
#     "key": "value",
#     "stream": "Cyber Security", # string
#     "completed_lessons": 3, # int
#     "complete_lessons_names": ["variables", "operators", "data_collections"]
# }
#
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










# #TASKS
#
# #task1
# name = 'Munira'
# age = 23
# birthday = 20/01/1998
# print('OMG', name, 'you are', age, 'years old so you were born in', birthday)
#
# #task2
# name = (input("what is your name"))
# age = (input("How old are you"))
# birthday = (input("please enter your birthday"))
#
# birth_date_passed = input("has your birthday passed already? YES/NO ")
#
#     print('your next birthday will be in 2022')
#
#
# # year_born = input("is this the correct year you are born enter yes or no")
# # if year_born == "no":
# #     born += 1
# #     print('OMG', name, 'you are', age, 'years old so you were born in', born)
# # else:
# #     print("thank you")