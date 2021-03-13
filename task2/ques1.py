
print("Hi Welcome")
num_test = eval(input("Please enter a number: "))


if(num_test%3 == 0 and num_test%5 == 0):
    print("Consultadd - Python Training")
elif(num_test%5 == 0):
    print("Python training ")
elif(num_test%3 == 0):
    print("Consultadd")
else:
    print("Try another no")

