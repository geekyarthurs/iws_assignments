string = input("Enter your string: ")

result = ""

if len(string) > 1:
    result = string[:2] + string[-2:]

print("Output: " + result)