"""def total_marks(n,data):
    data[0]=100
    n=200
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)
print(n)"""

#how many prime numbers are there in a list
"""from math import *
def isprime(num):
    if num==1:
        return 0
    s=int(sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def countPrimes(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
        
n=int(input())
data=list(map(int,input().split()))
pc=countPrimes(n,data)
print("prime count is: ",pc)"""

#printing prime numbers of a list
"""from math import *
def isprime(num):
    if num==1:
        return 0
    s=int(sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findPrimes(n,data):
    l=[]
    for i in data:
        if isprime(i):
            l.append(i)
    return l
        
n=int(input())
data=list(map(int,input().split()))
primes=findPrimes(n,data)
print(*primes)"""

#printing prime,nin prime numbers of a list
"""from math import *
def isprime(num):
    if num==1:
        return 0
    s=int(sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findPrimes(n,data):
    primes=[]
    np=[]
    for i in data:
        if isprime(i):
            primes.append(i)
        else:
            np.append(i)
    return primes,np
        
n=int(input())
data=list(map(int,input().split()))
primes,np=findPrimes(n,data)
print(*primes)
print(*np)"""

#sum of prime numbers
"""from math import *
def isprime(num):
    if num==1:
        return 0
    s=int(sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findPrimes(n,data):
    primes=[]
    np=[]
    for i in data:
        if isprime(i):
            primes.append(i)
        else:
            np.append(i)
    return sum(primes),sum(np)
        
n=int(input())
data=list(map(int,input().split()))
primes,np=findPrimes(n,data)
print(primes)
print(np)"""

#sum of digits with no return value
"""def sums(n):
    s=0
    while n:
        r=n%10
        n//=10
        s+=r
    return s
def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sums(data[i])
    return data
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)"""

#reverse the each and every element in the list
"""def reverse_digits(n):
    s=0
    while n:
        r=n%10
        n//=10
        s=s*10+r
    return s
def reverseofdigit(n,data):
    for i in range(len(data)):
        data[i]=reverse_digits(data[i])
    return data
n=int(input())
data=list(map(int,input().split()))
reverseofdigit(n,data)
print(*data)"""

#count of palindrome in list using functions with return value
def pali_count(n):
    temp=n
    rev=0
    while n:
        r=n%10
        n//=10
        rev=rev*10+r
    return rev==temp
def palindromecount(n,data):
    pc=0
    for i in range(len(data)):
        if pali_count(data[i]):
            pc=pc+1
    return pc
n=int(input())
data=list(map(int,input().split()))
print(palindromecount(n,data))
