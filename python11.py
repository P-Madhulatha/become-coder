num=int(input())
ec=0
oc=0
while num:
    r=num%10
    num//=10
    if r%2==0:
        ec+=1
    else:
        oc+=1
print("even count is",ec," and odd count is",oc,end='\n')
if ec%2==0:
    print("even",end=' ')
if oc%2!=0:
    print("odd",end=' ')
if ec%2 and oc%2==0:
    print("Mixed")
    
        
    
    
