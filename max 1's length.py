def max_sorted_length(n,data):
    if n==0:
        return 0
    c=0
    count=0
    for i in range(n):
        if data[i]==1:
            c+=1
        else:
            if count<c:
                count=c
            c=0
            
    return max(c,count)
n=int(input())
data=list(map(int,input().split()))
print(max_sorted_length(n,data))
