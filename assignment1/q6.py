string = input("Enter your string: ")

not_idx = string.find("not")
poor_idx = string.find("poor")

result = string 

if not_idx < poor_idx and not_idx != -1:
    first_part = string[:not_idx]
    middle_part = "good"
    last_part = string[poor_idx+4:]
    result = first_part + middle_part + last_part
    
print(result)