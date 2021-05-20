# russian piece of multiplication method
a,b=map(int,input().split())
res=0
while True: 
    if a%2:
        res+=b
    a==a//2
    b=b*2
    if a==0:
        break
print(res)

#another model using functions
def mul(a,b,res=0):
    while a:
        if a%2:
            res+=b
        a=a//2
        b=b*2
    return res

a,b=map(int,input().split())
res=mul(a,b)
print(res)

#colad sequence
     
n=int(input())
while n!=1:
    print(n,end=' ')
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
print(n)

#recursion model
    
def seq(n):
    if n==1:
        print(n,end=' ')
        return
    print(n,end=' ')
    if n%2:
        seq(3*n+1)
    else:
        seq(n//2)
n=int(input())
seq(n)
        
        


