# Ezrhael R. Sicat
# BSCpE 1-5
# 04/25/2023
# Write a method in python that will create two separate text files after reading 
# the source text file named integers.txt that contains 20 integers. The first 
# output file will be named double.txt containing the square of all even integers 
# found in integers.txt and the second file will be named triple.txt containing the 
# cube of all odd numbers found in the integers.txt.

# ask user for input
while True:
    user_input = input("How many numbers would you like to input? ")
    # looping to accept only valid number
    if not user_input.isnumeric():
        print("Invalid input. Please enter a valid number.")
    else:
        number_inputs = int(user_input)
        break

numbers = []
i = 0
while len(numbers) < number_inputs:
    # ask the user to enter the number
    num = input("Enter number {} of {}: ".format(i+1, user_input))
    # looping to accept only an integer number
    if not (num.isnumeric() or num.startswith('-') and num[1:].isnumeric()):
        print("Invalid input. Please enter a number.")
    else:
        numbers.append(num)
        i += 1

# write the numbers to the file
with open("numbers.txt", "w") as number_file:
    number_file.write(",".join(numbers))
# read the contents of the file
with open("numbers.txt", "r") as input_file:
    user_numbers = input_file.read().strip().split(",")
# loop through each number and add it to the appropriate list
odd_numbers = []
even_numbers = []
for number in user_numbers:
    if int(number) % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
# square the even numbers
# cube the odd numbers
# convert the list into string
# display output
# write odd and even numbers to files