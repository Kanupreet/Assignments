



class Prog1:
    a = 50
    b = 30
    def __init__(self,c):
        self.c = c
    def ans(self):
        y = 2*a*b
        z = y/self.c
        return z*z

inp = eval(input("Enter the value: "))
obj1 = Prog1(inp)

print(obj1.ans())


        
