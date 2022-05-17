# For the following list of numbers:

from cgitb import small
from operator import le
from unittest import skip


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []

for number in numbers:
    if(number % 2 == 0):
        even_numbers.append(number)
print(even_numbers)        

# 2. Print the difference between the largest and smallest value:
largest_number = 0
for number in numbers:
    if number > largest_number:
        largest_number = number

smallest_number = 100
for number in numbers:
    if number < smallest_number:
        smallest_number = number

difference = largest_number - smallest_number
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for index in range(len(numbers)):
    if numbers[index] == 2:
        if numbers[index + 1] == 2:
            print("True")

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

#  I've adopted this one from stack overflow!!!
#  stop statement let us skip the portion of numbers in a list
#  when stop set to True loop doesn't add up to sum until we find the matching number to continue
#  this was the easiest and simplest way I could find

def total_in_selection(array):
    sum = 0
    stop = False
    for num in array:
        if num == 6:
            stop = True
        elif num == 9:
            stop = False
        elif stop is False:
            sum = sum + num
    return sum

print(total_in_selection(numbers))
        
# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

lucky_sum = 0
lucky_list = numbers.copy()

for index, item in enumerate(lucky_list):
    if(item == 13):
        lucky_list.pop(index)
        lucky_list.pop(index)

for num in lucky_list:
    lucky_sum += num

print(lucky_sum)