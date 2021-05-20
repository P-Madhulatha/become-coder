#recusion in restian piece method
def mul(a,b):
    if a==0:
        return 0
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return mul(a//2,b*2)

a,b=map(int,input().split())
print(mul(a,b))

#generating of fibonacii series using recursions

def fibi(a,b,i,num):
    if i>num:
        return 
    if i==1 and i<=num:
        print(a,end=" ")
        i+=1
    if i==2 and i<=num:
        print(b,end=" ")
        i+=1
    if i<=num:
        print(a+b,end=" ")
    fibi(b,a+1,i+1,num)

num=int(input())
a=0,b=1
i=1
fibi(a,b,i,num)

#reverse the number by recusion

def rev(n,temp):
    if n:
        r=n%10
        temp=temp*10+r
        rev(n//10,temp)
    else:
        print(temp)

n=int(input())
rev(n,0)

