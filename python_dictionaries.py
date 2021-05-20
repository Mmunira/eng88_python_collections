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

from datetime import date
name = "Munira"
age = 23
current_year = date.today().year
birth_year = current_year - age
print("OMG", name, "you are", age, "years old so you were born in", birth_year)

name = input("What is your name")
age = int(input("how old are you"))

birthday = input("has your birthday already happened this year (Y/N) ")
if birthday == "Y":
    birth_year = current_year - age
else:
    birth_year = current_year - age - 1
print("OMG", name, "you are", age, "years old so you were born in", birth_year)

import time
date = time.strftime("%Y, %m, %d, %H").split(',')

current_month = int(date[1])
current_day = int(date[2])
current_hour = int(date[3])
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
hours_in_year = 365 * 24
total_days = 0
for i in range (current_month - 1):
    total_days += month_days[i]
total_days += current_day
total_hours = total_days * 24 + current_hour
if birthday == "Y":
    minimum_hours = age * hours_in_year
    maximum_hours = minimum_hours + total_hours
else:
    minimum_hours = age * hours_in_year + total_hours + 1
    maximum_hours = age * hours_in_year + hours_in_year - (24-current_hour)
print("you are between", minimum_hours, "and", maximum_hours, "hours old")


# current_month = date.today().month
# current_day = date.today().day
# total_year_days = 365

# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# current_year_days = 0
# for i in range (current_month-1):
#     current_year_days += month_days[i]
# current_year_days += current_day
# birth_year = int(current_year + current_year_days / total_year_days - age)
