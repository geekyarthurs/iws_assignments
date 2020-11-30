def case_counter(string: str) -> None:
    upcount = lowcount = 0
    for i in string:
        if i.isupper():
            upcount += 1
        elif i.islower():
            lowcount += 1
    
    print("Upcount: " + str(upcount))
    print("Lowcount: " + str(lowcount))
