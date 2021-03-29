




def strRev(str1):
    strLen = len(str1)
    for i in range(strLen - 1, -1, -1):
        yield str1[i]



val = strRev("Consultadd Training")
strFinal = ''
for ch in val:
    strFinal += ch
print(strFinal)

###val = strRev("Consultadd Training")
    
