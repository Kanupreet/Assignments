
def evalStr(str):
    l1 = []
    while str!="":
        l1.append(str.partition("-")[0])
        str = str.partition("-")[2]
    l1.sort()
    strFinal = '-'.join(l1)    
    return strFinal


str1 = "hi-how-are-you-doing"
print(evalStr(str1))
