#original numbers
"""def ori(n,data):
    k=[]
    for i in data:
        if i not in k:
            k.append(i)
    return k
n=int(input())
data=list(map(int,input().split()))
print(*ori(n,data))"""

#sorting method
"""def ori(n,data):
    data=list(set(data))
    data.sort()
    return data
n=int(input())
data=list(map(int,input().split()))
print(*ori(n,data))"""

#match count
"""def original(n,data):
   k=[]
   c=0
   for i in data:
       if i not in k:
           k.append(i)
   for i in range(len(k)):
        if data[i]==k[i]:
            c+=1
   return c
n=int(input())
data=list(map(int,input().split()))
c=original(n,data)
print(c)"""

#match count for sorted list
def original(n,data):
    k=[]
    c=0
    for i in data:
        if i not in k:
            k.append(i)
    k=list(set(data))
    for i in range(len(k)):
        if data[i]==k[i]:
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
c=original(n,data)
print(c)
        
        
    
