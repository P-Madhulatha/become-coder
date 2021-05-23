#lcm of two numbers
'''
t  a   b
2 12  24
---------
2  6   12
---------
3   3   6
---------
    1   2-----24[lcm]
'''
#normal method
'''a,b=map(int,input().split())
t=2
res=1
while True:
    if a%t==0 and b%t==0:
        res=res*t
        a//=t
        b//=t
    else:
        t+=1
    if a<t or b<t:
        break
print(res*a*b)'''

#using functions
"""def lcm_num(a,b):
    if a>b:
        big=a
    else:
        big=b
    while True:
        if((big%a==0) and (big%b==0)):
            lcm=big
            break
        big+=1
    return lcm

a,b=map(int,input().split())
print(lcm_num(a,b))"""

#another method
"""def lcm(a,b):
     t=2
     res=1
     while a>=t and b>=t:
         if a%t==0 and b%t==0:
             a=a//t
             b=b//t
             res=res*t
         else:
              t+=1
     return res*a*b

a,b=map(int,input().split())
print(lcm(a,b))"""

#recusion model
def lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return lcm(a,b,t+1)

a,b=map(int,input().split())
print(lcm(a,b,2))
             
           
         
