string = input("Enter your string: ")

new_str = first_char = string[0]



for i in string[1:]:
    if i == first_char:
        new_str += "$"
    else:
        new_str += i

print(new_str)