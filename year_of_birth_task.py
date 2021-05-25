# Create program that calculates the year of birth.
#
# ## Tasks
#
# * define the variables `age` and `name`
# * make a calculation for the year in which the person was born
# * print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values
#
# ### Second Part
#
# * prompt the user for input and re-assign the variable `age` and `name`
# * figure out a way to account for if the persons birthday has already happened this year or not
#
# ### Extra
#
# * go look into the library time
# * print out the amount of hour this person has lived
#
# ## Acceptance Criteria
#
# * program defines the variable `age` and `name`
# * program prints the string "OMG <person>, you are <age> years old so you were born in <year>"


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
