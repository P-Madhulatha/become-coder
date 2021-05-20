#generating fibonocii
def gen_fib(num,a=0,b=1):
    if num==0:
        return
    if num==1:
        print(a)
        return
    print(a,b,end=' ')
    for i in range(3,num+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        
num=int(input())
gen_fib(num)

# fibanocii in range      
def gen_fib(l,u,a=0,b=1):
    if l==0:
        print(a,b,end=' ')
    if l==1:
        print(b,end=' ')
    c=0
    while c<=u:
       if c>=l and c<=u:
       a=b
        b=c
l,u=map(int,input().split())
gen_fib(l,u)
            
#is num is fib or not
def isfib(n):
      if n==0 or n==1:
        return True
        a=0
        b=0
      while True: 
         c=a+b
         if c==n:
             return True
         if c>n:
             return False
         a=b
         b=c
T=int(input())
for _ in range(T):
    n=int(input())
    print(isfib(n))

#printing nearest values of fib

def fib(n):
    if n==0 or n==1:
        return True
    a=0
    b=1
    while True:
        c=a+b
        if c==n:
            return True
        if c>n:
            print(b,n,c)
            if n-b >= c-n:
                print(c)
            if n-b <= c-n:
                print(b)
            return False
        a=b
        b=c
        
n=int(input())
print(fib(n))
        
