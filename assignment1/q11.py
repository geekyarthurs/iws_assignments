string = input("Enter your string: ")

string = string.replace(".", "") #removing fullstop.

string_list = string.split(" ")

counts = dict()

for sx in string_list:

    counts[sx] = counts.get(sx, 0) + 1

print(counts)

# I have ignored .lower()