"""n=int(input())           
data=[]                           
for i in range(n):           
    val=int(input())
    data.append(val)
print(data)"""

#another method without appending
"""n=int(input())
data=[None for i in range(n)]
for i in range(n):
    val=int(input())
    data[i]=val    #placing the value in list
print(data)"""

#taking the input in single line
"""n=int(input())
data=list(map(int,input().split()))
print(data)"""

#index based
"""n=int(input())
data=list(map(int,input().split()))
for i in range(n):
    print(i,data[i])"""

#value based
"""n=int(input())
data=list(map(int,input().split()))
for i in data:
    print(i,end=" ")"""
#sum of list of elememts
"""n=int(input())
data=list(map(int,input().split()))
res=0
for i in range(n):    #index based
    res=res+data[i]
    print(res)"""
#value based
"""n=int(input())
data=list(map(int,input().split()))
res=0
for i in data:
    res=res+i
print(res)"""

#using functions
"""def total_marks(n,data):
    res=0
    for i in data:
        res+=1
    return res
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)"""

#usinf functions with return value[count of even and odd]
def total_marks(n,data):
    ec,oc=0,0
    for i in range(n):
            if data[i]%2==0:
                ec+=1
            else:
                oc+=1
    return ec,oc
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(*total)
        


          

          
         


