### Execute to understand chronology of Decorator

def divSpecial(fxn):
    print("fxn start")
    def inner(a,b):
        print("Before if")
        if a<b:
            a,b = b,a
        return fxn(a,b)
    print("Before Inner")
    return inner

@divSpecial
def div(a,b):
    print(a/b)
    print("in fxni")
    return a/b


print(div(2,4))
