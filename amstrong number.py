#amstrong or not

n=int(input())
order=len(str(n))
sum=0
temp=n
while temp>0:
    r=temp%10
    sum+=r**order
    temp//=10
if n==sum:
    print(n,"is an amstrong number")
else:
    print(n,"is not an amstrong number")
