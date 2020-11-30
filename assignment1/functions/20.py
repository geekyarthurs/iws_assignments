arr1 = [1,2,3]
arr2= [3,4,5]

intersection = lambda a1, a2: [ x for x in arr1 for y in arr2 if x == y ]

print(intersection(arr1, arr2))