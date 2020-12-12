my_info = ("Mahesh", "Regmi", 19)

people = []

people.append(my_info)
people.append(("Ram", "Shrestha", 20))
people.append(("Ankita", "Tamang", 35))

people.sort(key=lambda x: x[-1])

print(people)