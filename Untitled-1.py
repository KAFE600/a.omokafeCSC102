#Finding the roots of a cubic equation using Cardano's Formula
#Step one
a1 = input("Emter your a1 :")
a2 = input("Enter your a2 :")
a3 = input("Enter your a3 :")

print(a1)
print(a2)
print(a3)

#Step Two
Q = (3*int(a2) - int(a1)^2)/9
R = (9*int(a1)*int(a2) - 27*int(a3) - 2*int(a1)^3)/54
print(Q)
print(R)

#Step Three
S = (int(R) + (int(Q)^3 + int(R)^2)**1/2)**1/3
T = (int(R) - (int(Q)^3 + int(R)^2)**1/2)**1/3


#Step Four
X1 = int(S) + int(T) - 1/3*int(a1) 
X2 = -1/2*(int(S) + int(T)) - 1/3*int(a1) + 1/2 
X3 = -1/2*(int(S) + int(T)) - 1/3*int(a1) - 1/2

print("The first root is:".X1)
print("The second root is".X2)
print("The third root is:".X3)


