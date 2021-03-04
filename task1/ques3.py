
print("Ques3")

a = 25
b = 100

print("Original values of var1: " , a )
print("Original values of var2: " , b )

c=b
b=a
a=c
print("After swapping with 3rd var")
print("Final values of var1: " , a )
print("Final values of var2: " , b )

a , b = b, a
print("After swapping without any var")
print("Final values of var1: " , a )
print("Final values of var2: " , b )
