#disarium number

def isdisarium(num):
    dc=0
    temp=num
    while temp:
        temp=temp//10
        dc+=1
    temp=num
    res=0
    while temp:
        r=temp%10
        temp//=10
        res=res+pow(r,dc)
        dc-=1
    return res==num
num=int(input())
print(isdisarium(num))
    
