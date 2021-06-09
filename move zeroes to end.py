#move zeros
def movezeros(n,data):
    for i in range(n):
        if data[i]==0:
            data.insert(n,0)
            data.remove(0)
        
n=int(input())
data=list(map(int,input().split()))
movezeros(n,data)
print(*data)
