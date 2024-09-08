def remove_odd_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:  #<- To check if the number is even
            even_numbers.append(num)
    return even_numbers

#Test list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_odd_numbers(original_list)
print(f"Original list: {original_list}")
print(f"List with odd numbers removed: {filtered_list}")