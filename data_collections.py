# Lists
# Syntax ["London"]
# CRUD CREATE READ UPDATE DELETE

# WHAT ARE LISTS?
# LISTS ARE MUTABLE

# shopping_list = ["juice", "strawberries", "yogurt", "chicken", "raspberries", "butter"]
#               #      0           1             2          3            4           5
# print(shopping_list)
# print(type(shopping_list))
#
# print(shopping_list[2])
# print(shopping_list[4])
# print(shopping_list[-1])
#
# # if we needed to replace something from the list
# shopping_list[5] = "oats"
# print(shopping_list)
#
# # if we needed to add something to a list we have a method called append
# shopping_list. append("Mango")
# print(shopping_list)
#
# # if we want to remove something from a list we have a method called remove
# shopping_list.remove("oats")
# print(shopping_list)
#
# # if we want to remove the last item from a list we use pop
# shopping_list.pop()
# print(shopping_list)

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


