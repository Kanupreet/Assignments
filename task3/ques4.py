


l1 = [44,77,89,76,34,84,56,87,98,78,92]
lar_num = l1[1]
small_num = l1[1]

for i in l1:
    if i > lar_num: 
        lar_num = i
    if i < small_num:
        small_num = i


print("Printing list: ", l1) 
print("Printing Smallest no: ", small_num) 
print("Printing Largest no: ", lar_num) 


