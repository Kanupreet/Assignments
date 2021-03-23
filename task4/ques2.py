

def strCount(str):
    upCase = 0
    loCase = 0
    for s in str:
        if s.isupper():
            upCase += 1
        if s.islower():
            loCase += 1
    print("String is: ", str)
    print("Total no of uppercase letters: ", upCase)
    print("Total no of lowercase letters: ", loCase)

inpstr = input("Please enter the input string: ")

strCount(inpstr)
