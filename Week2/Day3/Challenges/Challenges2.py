# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****

rows = 3
for i in range(rows):
    spaces = rows - 1 - i
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)


# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

rows = 5
for i in range(1, rows + 1):
    spaces = rows - i
    stars = i
    print(" " * spaces + "*" * stars)

# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *

rows = 5

# up (1 to 5)
for i in range(1, rows + 1):
    print("*" * i)

# down (5 to 1) with leading spaces
for i in range(rows, 0, -1):
    spaces = rows - i
    print(" " * spaces + "*" * i)


# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if(my_list[j] < my_list[minimum]):
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)


my_list = [2, 24, 12, 354, 233]  # initial list

for i in range(len(my_list) - 1):  # i goes 0..3
    minimum = i  # assume the smallest value is at index i

    for j in range(i + 1, len(my_list)):  # j checks every index after i
        if my_list[j] < my_list[minimum]:  # found a smaller value
            minimum = j  # update index of the smallest value found so far

            # NOTE: This swap is inside the IF, so it swaps immediately after finding a smaller value
            if minimum != i:
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]  # swap positions

print(my_list)  # prints the final list

#[2, 12, 24, 233, 354]
