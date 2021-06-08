def max_sorted_length(n,data):
    c=1
    mc=0
    for i in range(n-1):
        if data[i]<data[i+1]:
            c+=1
        else:
            if mc<c:
                mc=c
            c=1
    if mc<c:
        return c
    return mc
n=int(input())
data=list(map(int,input().split()))
print(max_sorted_length(n,data))
