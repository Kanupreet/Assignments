

d1 = {1:10,2:20}
d2 = {3:30,4:40}

print("First Dictionary: ", d1)
d3 = d1
d3.update(d2)


print("First Dictionary: ", d1)
print("Second Dictionary: ", d2)
print("Merged Dictionary:", d3)
