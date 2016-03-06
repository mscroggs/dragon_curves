from random import choice

def dragon(n):
    if n==1:
        return [1]
    prev = dragon(n-1)
    return prev + [1]+ swap_middle(prev) 

def swap_middle(ls):
    mid = len(ls) / 2
    ls[mid] = 1-ls[mid]
    return ls

for n in range(1,20):
    print n,sum(dragon(n)),len(dragon(n))-sum(dragon(n))
