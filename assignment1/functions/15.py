numbers = [13,15,30,35,20]

filtered_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(filtered_numbers))