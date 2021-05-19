#what are dictionaries?
#are structured as KEY = VALUE
#VALUE could be string, int, list
#Syntax {}

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


#TASKS

print(student_1["complete_lessons_names"][1])

name = 'Munira'
age = 23
born = 98
print('OMG', name, 'you are', age, 'years old so you were born in', born)

name = input("what is your name")
age = input("what is your age")

born = 2021 - int(age)
print('OMG', name, 'you are',age, 'years old so you were born in', born)

year_born = input("is this the correct year you are born enter yes or no")
if year_born == "no":
    born += 1
    print('OMG', name, 'you are', age, 'years old so you were born in', born)
else:
    print("thank you")