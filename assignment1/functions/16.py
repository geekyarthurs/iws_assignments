numbers = [13,15,30,35,20]

squares = map(lambda x: x ** 2, numbers)
cubes = map(lambda x: x ** 3,numbers)

print(list(squares))
print(list(cubes))