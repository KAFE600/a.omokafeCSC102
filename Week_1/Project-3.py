# A python program to solve a annunity plan problem. 


PMT = input("Insert the PMT :")
Rate = input("Insert the rate :")
n = input("Insert the n :")
t = input("Insert the t :")
Final_Amount = int(PMT) * (1 + int(Rate)/int(n))**(int(n)*int(t)) - 1/(int(Rate)/int(n))


print(PMT)
print(Rate)
print(n)
print(t)
print(Final_Amount)






