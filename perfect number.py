#perfect number
#"""
#factors of num  and add all numbers to get the same value
#28=2+4+7+14
#"""


import math as m
def isperfect(num):
    res=1
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            res+=i+num//i
    return res==num

num=int(input())
print(isperfect(num))

#using recursions
import math as m
def isperfect(num,n):
    if n==int(m.sqrt(num)):
        if num%n==0:
            return n+1
        return 1
    if num%n==0:
        return n+num//n+isperfect(num,n+1)
    return 0+isperfect(num,n+1)
num=int(input())
print(num==isperfect(num,2))
