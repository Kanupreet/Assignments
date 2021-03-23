

def compStr(str1,str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1)
        print(str2)


inpStr1 = input("Please enter the 1st String: ")
inpStr2 = input("Please enter the 2nd String: ")

compStr(inpStr1,inpStr2)
