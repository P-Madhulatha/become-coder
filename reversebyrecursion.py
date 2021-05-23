def rev(num):
    if num==0:
        return 1
    return (num//10)*10+(num%10)

num=int(input())
print(rev(num))
