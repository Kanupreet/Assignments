

print("Printing new list")



l1 = []
for i in range(1,31):
    if i<6 or i>25:
        l1.append(i**2)
    else:
        l1.append(i)


print("Final list: ", l1)
