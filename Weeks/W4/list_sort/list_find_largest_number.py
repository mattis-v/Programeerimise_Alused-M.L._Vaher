'''
Create a function that takes a list of numbers and returns the second largest number.
'''
# import random

list1 = [8623,62,8623,453.67,476,890.01,1102,3102,11,89,56,2112.5]
list2 = [21]
list3 = [-21,-100,-69,-420,-67]
list4 = []
list5 = [-21,-100,69,420,67]

def second_largest_manual_sort(lst):
    # initial setpoint in negative infity for variables.
    # setpoint=0 would not work as intended with negative values in list.
    
    last_largest = float('-inf')
    largest = float('-inf')
    
    # determines the largest number in list.
    for number in lst:
        if number > largest:
            largest = number

    # determines the second largest number in list.
    # last largest must be larger than number, smaller than largest and not largest.
    for number in lst:
        if number > last_largest and last_largest < largest and number != largest:
            last_largest = number
    
    # incase list contains fewer than 2 numbers, otherwise would return -inf as second largest.
    if last_largest == float('-inf'):
        return("incomplete list")


    return last_largest

print("From list 1: ",second_largest_manual_sort(list1),"\n")

print("From list 2: ",second_largest_manual_sort(list2),"\n")

print("From list 3: ",second_largest_manual_sort(list3),"\n")

print("From list 4: ",second_largest_manual_sort(list4),"\n")

print("From list 4: ",second_largest_manual_sort(list5))