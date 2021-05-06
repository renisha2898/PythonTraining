import cmath
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
def quadEquation():
    d=(b**2)-(4*a*c)
    quad1=(-b-cmath.sqrt(d))/(2*a)
    quad2=(-b+cmath.sqrt(d))/(2*a)
    if quad1 or quad2 <=0:
        return None,None
    else:
        return quad1,quad2


if __name__ == '__main__':
    x,y=quadEquation()
    print(x,y)

