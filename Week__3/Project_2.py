# A python program for one of the top four FinTechs in Nigeria with about 2500 staff strength with various years of work experience. 
def staff():
  Experience= int(input("Enter the years of exprience :"))
  Age = int(input("Enter the age of the staff :"))

# ATR(Annual Tax Revenue)
  for Experience in range(2500):

#If Staff
  if Experience > 25 and Age >= 55:
    print("ATR is N5,600,000")

#If Staff
  elif Experience > 20 and Age >= 45:
    print("ATR is N4,480,000")

#If Staff
  elif Experience > 20 and Age >= 35:
    print("ATR is N1,500,000")

#If Staff
  elif Experience < 10 and Age < 35:
    print("ATR is N550,000")

  else:
    print("You are not a staff!")
    print("Do you want to try again? ")
print("Program to check the ATR of Staff ")
decicion = int(input("1. YES or 2. NO "))
if decision == 1:
  staff()
elif decision == 2:
  print("Program timeout")