'''

Generators are the self created iterators we can create in python. Yield is the keyword used to create it.
To access created generator(self created iterator), we can use 2 methods to access it:
1. using __next__  - We can simple get it by printing val.__next__ (val is a var to store result of a fxn)one by one. But problem here is we have to write as many __next__ as values are there.
2. We can use a loop to print it out - for i in val: print(i)


Why use generator?
In case, you want to fetch values from db to perform some fxn, there is no point fetching all the values and loading memory. You can fetch the needed values and use them without overloading the memory.
Ex - in general, either you will fetch all values or apply code and store them in list or something and then access list or something for further fxn. With yeild you can directly get values and work with them.

'''

def genTry():
    i = 1
    while i <= 10:
        sq = i*i
        yield sq
        i+= 1


val = genTry()

for x in val:
    print(x)




 
