string = input("Enter your string: ")
string2 = input("Enter your second string: ")


result = f"{string2[:2]}{string[2:]} {string[:2]}{string2[2:]}"

print(result)