


print("Creating a problem of entering no in tuple and List")
inp = eval(input("Enter numbers seperated by comma: "))
l1=[]
for i in inp:
    l1.append(str(i))
t1 = tuple(l1)
print("\nList from your entered Result: ",l1)
print("Tuple from your entered Result", t1)
