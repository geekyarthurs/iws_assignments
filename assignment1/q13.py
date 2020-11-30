raw_list = input("Enter your string: ")

str_list = raw_list.split(", ")

str_list.sort()

print(*str_list, sep=", ")