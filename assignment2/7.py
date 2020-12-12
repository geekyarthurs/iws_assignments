my_friends = [("Bibek", "Dhungana", 20), ("Ram"), ("Shrestha"), 18]

age_sum = 0
for fname, lname,age in my_friends:
    if age:
        age_sum += age

avg_age = age_sum / len(my_friends)

print(f"Average Age: {avg_age}")
