



def limitLabel(limit):
    for i in range(0,limit+1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")
   


inp = eval(input("Please enter the limit range: "))
limitLabel(inp)
