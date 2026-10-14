def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: 3 & 4, 
# number = 1: The if number > 1 condition checks whether $1 > 1$, which is False.
# number = 2: The condition checks whether $2 > 1$, which is True.
# number = 3: The condition checks whether $3 > 1$, which is True. 
# The loop executes add_one(3), which evaluates to 4, and print() displays 4.


# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: 3 
# return inside the function Passes the computed result back to the caller so it can be stored in a variable, passed to another function, or used in further calculations.
# print in the loop takes a value and displays it as text output in the console for human viewing. It does not send a value back to the program logic or alter data flow.