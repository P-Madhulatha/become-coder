def leaders(n,data):
    for i in range(n-1):
        if data[i]==max(data[i:]):
            k.append(data[i])
    return k
n=int(input())
k=[]
data=list(map(int,input().split()))
print(*leaders(n,data))
