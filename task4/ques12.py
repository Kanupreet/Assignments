def divTest(num1,num2):
    try:
       return num1/num2
    except:
        print("cannot be divided by 0")

inp1 = eval(input("Enter 1st number: "))
inp2 = eval(input("Enter 2nd number: "))
print(divTest(inp1,inp2))
