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
