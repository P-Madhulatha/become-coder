#GCD program
"""
GCD:
a   b
26  12    ---we have to manitain smaller and bigger
12  26  ---swapping
12  26%12  ----bigger%smaller
12  2
2   12
2   12%2
2    0
"""

def gcd(a,b):
    while True:
        if a>b:
            a,b=b,a
        b=b%a
        if b==0:
            return a
a,b=map(int,input().split())
print(gcd(a,b))

#recursion model

        
def gcd(a,b):
        if a>b:
            a,b=b,a
        a,b=a,b%a
        b=b%a
        if b==0:
            return a
        else:
            gcd(a,b)
a,b=map(int,input().split())
print(gcd(a,b))
