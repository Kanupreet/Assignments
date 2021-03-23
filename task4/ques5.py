

'''
def strUpper(str):
    li = []
    while str != "":
        li.append(str.partition(" ")[0])
        str = str.partition(" ")[2]
    for i in li:
        i.upper()
    str2 = ' '.join(li)
    return str2
'''

inpStr = input("Please enter your string: ")
##print(strUpper(inpStr))
print(inpStr.upper())

