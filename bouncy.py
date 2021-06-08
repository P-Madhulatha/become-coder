"""def bouncy(n,data):
    l=data[0]
    h=data[1]
    if l>h:
        l=1
        h=0
    else:
        h=1
        l=0
    for i in range(1,n-1):
        if l and data[i]<data[i+1]:
            h=1
            l=0
        if h and data[i]>data[i+1]:
            l=0
            h=0
        else:
            return False
    return True
            
n=int(input())
data=list(map(int,input().split()))
print(bouncy(n,data))"""

#another one
def bouncy(n,data):#1 4 2 3 4
    l=data[0]
    h=data[1]
    if l<h:#1<4
        h=True
        l=False
    else:
        l=True
        h=False
    for i in range(1,n-1):#4 2 3 4
        #h=True and 4<2
        
        if (h==True and data[i]<data[i+1]) and (l==True and data[i]>data[i+1]):
            return False
        h=not h
        l=not l
    return True
            
n=int(input())
data=list(map(int,input().split()))
print(bouncy(n,data))
