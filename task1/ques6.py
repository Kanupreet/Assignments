print("Hi I will let you know the data type of your input")
print("Enter your value")

a = (input())

if a.isalnum():
    print("Its an integer value")
elif a.isdecimal():
    print("Its a float value")
else:
    print("Its a string")
'''
b = type(a)
print(b)

if b == int:
    print("Its an Integer value")
elif b == str:
    print("Its a String value")
elif b == float:
    print("Its a float value")
else:
    print("Invalid value")'''
