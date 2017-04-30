import math

def fromRightToLeft(aString):
    # permutation base 2 to base 10
    return int(math.pow(2,len(aString)) + int(aString,2) - 2)

def fromLeftToRight(aNumber):
    # base 10 to permutation base 2
    n = 1
    while(aNumber > 0):
        aNumber -= pow(2,n)
        n += 1
    n -= 1
    form = "{0:0" + str(n) + "b}"
    return form.format(aNumber + pow(2,n))

leftToRight = True
while(True):
    inp = input()
    if inp == "lr":
        leftToRight = True
    elif inp == "rl":
        leftToRight = False
    else:
        print(fromLeftToRight(int(inp))) if leftToRight else print(fromRightToLeft(inp))
