# *rows and columns patterns program
"""n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()"""

#printing series numbers(12345 for 5 rows)
"""n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end='')
    print() """

#printing same number for a row
"""n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end='')
    print() """

#adding i and j
"""n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i+j,end='')
    print() """

#printing reverse order[ex:54321]
"""n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end='')
    print() """

#printing even row with reverse order and odd row with normal
"""n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(n,0,-1):
            print(j,end='')
        print()
    else:
        for j in range(1,n+1):
            print(j,end='')
        print() """
#printing odd number of rows with same number[ex:11111]
"""n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,n+1):
            print(i,end='')
        print()
    else:
        for j in range(1,n+1):
            print(j,end='')
        print() """

#printing differnt numbers in 1st column
"""n=int(input())
for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1:
                print(i,end='')
            else:
                print(j,end='')
        print() """

#printing odd number of rows with reverse order and even with same number
"""n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(n,0,-1):
            print(j,end='')
        print()
    else:
        for j in range(1,n+1):
            print(j,end='')
        print() """

#printing the in put in the forms of 0's and 1's[ex:10101]
"""n=int(input())
for i in range(1,n+1):
        for j in range(1,n+1):
            if j%2==0:
                print(0,end='')
            else:
                print(1,end='')
        print() """

#replacing 0's with 1's for even rows
n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,n+1):
            if j%2==0:
                print(0,end='')
            else:
                print(1,end='')
        print()
    else:
        for j in range(1,n+1):
            if j%2==0:
                print(1,end='')
            else:
                print(0,end='')
        print()
        




