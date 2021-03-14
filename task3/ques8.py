

d1 = {1:10,2:20}
d2 = {3:30,4:40}

d3 = dict(d1,**d2)

for i in d1.values():
   print(i)

print(d1)
print(d2)
print(d3)
