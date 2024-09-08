def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#Test list
my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(f"The list is: {my_list}")
print(f"The sum of all numbers in the list is: {result}")