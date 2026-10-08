"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a list is being guven as a input 
# 2. Process:we show the different orders like ascending, descending, random and reverse
# 3. Out:we print the different forms the list can be modified
# 4. My four orders, and which ones modify the original:none of those modifies the original list 


# Your code below

import random

list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

print("Original list:", list_of_numbers)

print("1. Ascending:", sorted(list_of_numbers))

print("2. Descending:", sorted(list_of_numbers, reverse=True))

print("3. Reverse:", list_of_numbers[::-1])

random_order = list_of_numbers.copy()
random.shuffle(random_order)
print("4. Random order:", random_order)

print("Original list:", list_of_numbers)