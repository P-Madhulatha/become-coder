def max_sorted_length(n,data):#1 2 3 4 5 4 3 2 6 5 9
    c=1
    mc=0
    for i in range(n-1):#1 2 3 4 5 4 3 2 6 5 9
        if data[i]<data[i+1]:#5<4
            c+=1#c=3
        else:
            if mc<c:#0<5
                mc=c#c=0
            c=1
    if mc<c:#0<2
        return c#2
    return mc
n=int(input())
data=list(map(int,input().split()))
print(max_sorted_length(n,data))
