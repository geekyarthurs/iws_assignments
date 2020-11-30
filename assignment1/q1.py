string = input("Enter your string: ")

counts = dict()

for char in string:
    counts[char] = counts.get(char,0) + 1

print(counts)
