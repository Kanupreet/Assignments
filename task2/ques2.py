print("Please enter values for Operation")
num1 = eval(input("Please enter 1st value: "))
num2 = eval(input("Please enter 2nd value: "))
print("\n\nHi Please enter any 1 option for the operation")
print("1-Addition   2-Subtraction   3-Division   4-Multiplcation   5-Average")
oper = eval(input("Please enter your response for operation: "))


if oper == 1:
    num3 = num1+num2 
elif oper == 2:
    num3 = num1-num2 
elif oper == 3:
    num3 = num1/num2 
elif oper == 4:
    num3 = num1*num2 
elif oper == 5:
    print("This option requies you to enter values again")
    num1 = eval(input("Please enter 1st value: "))
    num2 = eval(input("Please enter 2nd value: "))
    num4 = num1 + num2
    num3 =  num4/2
else:
    print("Not correct no for operation")


if num3 > 0:
    print("Answer is", num3)
else:
    print("Negative Number")

