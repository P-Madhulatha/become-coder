#original numbers
def ori(n,data):
    k=[]
    for i in data:
        if i not in k:
            k.append(i)
    return k
n=int(input())
data=list(map(int,input().split()))
print(*ori(n,data))

#sorting method
def ori(n,data):
    data=list(set(data))
    data.sort()
    return data
n=int(input())
data=list(map(int,input().split()))
print(*ori(n,data))
