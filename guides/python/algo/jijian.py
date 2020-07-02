#!/usr/bin/python3

def change(x):

    if x<0:
        return (-change(-x)[0], -change(-x)[1])
    elif x==5:
        return (1,0)
    elif x==7:
        return (0,1)
    else:
        if x > 7 and x%5 != 0:
            return (change(x-7)[0],change(x-7)[1]+1)
        elif x > 5:
            return (change(x-5)[0]+1,change(x-5)[1])
        else:
            # im not sure what to do here
            print(x)
            return None

print(change(-5))
print(change(-7))
print(change(5))
print(change(7))
print(change(5+7))
print(change(2*5+7))
print(change(2*5+2*7))
print(change(3*5+2*7))
print(change(1*5+2*7))
print(change(4*5+3*7))
print(change(4*5+1*7))
print(change(24))
print(change(25))
