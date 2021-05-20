#printing numbers of even and odd separately
num=int(input())
even=0
odd=0
ec=1
oc=1
while num:
    r=num%10
    num//=10
    if r%2==0:
        even=even+r*ec
        ec=ec*10
    else:
        odd=odd+r*oc
        oc=oc*10
print(even,odd,end=' ')

#replacing number
n,sv,rv=map(int,input().split())
nn=0
c=1
while n:
    r=n%10
    n//=10
    if r==sv:
        r=rv
    nn=nn+r*c
    c=c*10
print(nn)

#replacing multiples of searching value
n,sv,rv= map(int,input().split())#43256 2 1
nn=0
c=1
while n:
    r=n%10#6
    n//=10#432560
    if r%sv==0:
        r=rv*(r//sv)
    nn=nn+(r)*c
    c=c*10
print(nn)
        
        
    

