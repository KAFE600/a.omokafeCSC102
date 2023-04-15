#Finding the roots of a quadartic equation  [ax^4 + bx^3 + cx^2 + dx + e = 0]
a = float(input("Enter your a :"))
b = float(input("Enter your b :"))
c = float(input("Enter your c :"))
d = float(input("Enter your d :"))
e = float(input("Enter your e :"))

print(a)
print(b)
print(c)
print(d)
print(e)

P = (8*a*c - 3*b**2)/(8*a**2)
Q = (b**3 - 4*a*b*c + 8*a**2*d)/(8*a**3)
R = (-3*b**4 + 256*a**3*e - 64*a**2*b*d + 16*a*b**2*c)/(256*a**4)

U1 = 1/2**((-2*P/3) + (1/3)*1/2**(P**2 - 4*Q/3))
U2 = 1/2**((-2*P/3) - (1/3)*1/2**(P**2 - 4*Q/3))
    
V1 = (b/(4*a)) + (U1 + U2)/2
V2 = (b/(4*a)) - (U1 + U2)/2
    
    
W1 = 1/2**(2*U1 - P - (4/3)*Q/U1)
W2 = 1/2**(2*U2 - P - (4/3)*Q/U2)
    
    
    
X1 = (b**2 - 8*a*c)/(4*a*(U1 + W1))
X2 = (b**2 - 8*a*c)/(4*a*(U1 - W1))
X3 = (b**2 - 8*a*c)/(4*a*(U2 + W2))
X4 = (b**2 - 8*a*c)/(4*a*(U2 - W2))
    
roots = [V1 - X1/2 - 1/2**(X1**2 - 4*V1*X1)/2, 
             V1 - X1/2 + 1/2**(X1**2 - 4*V1*X1)/2, 
             V2 - X2/2 - 1/2**(X2**2 - 4*V2*X2)/2, 
             V2 - X2/2 + 1/2**(X2**2 - 4*V2*X2)/2, 
             V1 - X3/2 - 1/2**(X3**2 - 4*V1*X3)/2, 
             V1 - X3/2 + 1/2**(X3**2 - 4*V1*X3)/2, 
             V2 - X4/2 - 1/2**(X4**2 - 4*V2*X4)/2, 
             V2 - X4/2 + 1/2**(X4**2 - 4*V2*X4)/2]
print(roots)

