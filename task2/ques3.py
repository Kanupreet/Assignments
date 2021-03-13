
a = 10
b = 20
c = 30

avg = (a+b+c)/3
print("Average is", avg)

if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, c")
elif avg > a and avg > b:
    print("avg is higher than a,b")
elif avg > a and avg > c:
    print("avg is higher than a,c")
elif avg > b and avg > c:
    print("avg is higher than b,c")
elif avg > a:
    print("avg is higher than a")
elif avg > b:
    print("avg is higher than b")
elif avg > c:
    print("avg is higher than c")
else:
    print("Inconclusive")
