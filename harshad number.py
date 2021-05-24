def isharshad(num):
    sum=0
    while num:
        r=num%10
        num//=10
        sum+=r
    if num%sum==0:
        return True
    else:
        return False
num=int(input())
print(isharshad(num))
