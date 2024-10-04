for i in range(30):
    if i %3 and i %5 == 0:
        print("FuzzBizz")
    elif i %3 == 0:
        print("Fuzz")
    elif i %5 == 0:
        print("Bizz")
    else:
        print(i)