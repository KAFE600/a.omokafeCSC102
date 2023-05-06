tm1 = input("Enter the location of the product to be delivered: ")
tm2 = int(input("Enter the package weight:"))
    
def printinfo( tm1, tm2):
     if tm1 == 'ibeju lekki' and tm2 >= 10:
       print("The User paid 2000 Naira for a package with a weight of 10kg(or more) at Ibeju Community)");
     elif tm1 != 'ibeju lekki' and tm2 <= 9 :
        print("The User paid 1500 Naira for a package with a weight of 10kg(or more) at Ibeju Community)");
     if tm1 == "epe" and tm2 >= 10:
      print("The User paid 5000 Naira for a package with a weight of 10kg(or more) at Epe");
     elif tm1 != "epe" and tm2 <= 10:
       print("The User paid 4000 Naira for a package with a weight of 10kg(or more) at Epe");
     return; 
   
printinfo(tm1,tm2);

