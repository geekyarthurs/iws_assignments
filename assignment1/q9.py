string = input("Enter your string: ")


f, *rem, l = string

result = l + "".join(rem) + f

print(result)