from math import *
#for circle
r,l,b=map(int,input().split())
area=pi*(r**2)
dia=2*r
circum=2*pi*r
print("area of a circle:",round(area,2),"\ndiameter of a circle:",round(dia,2),"\ncircumference of a cicle:",round(circum,2),end=' ')
# for rectangle
ar=l*b
peri=2*(l+b)
d=(pow(l,2)+pow(b,2))**0.5
print("\narea of a rectangle:",round(ar,2),"\nperimeter of a rectangle:",round(peri,2),"\ndiameter of a reactangle:",round(d,2),end=' ')
