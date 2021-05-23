#factors of a number
"""
10---->4
100---->9
25--->1 5 25

is 100 is divisible by 2 or not and how many times
 2 50
 4 25
 5 20
 10
"""
import math as m
def factors_count(num):
    count=2
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            if i!=(num//i):
                count+=2
            else:
                count+=1
    print(count)
num=int(input())
factors_count(num)
    
