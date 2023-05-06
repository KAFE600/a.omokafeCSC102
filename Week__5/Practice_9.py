total = 50;
def sum(arg1, arg2):
    # Add both the parameters
    total = arg1 + arg2;
    print("Inside the function local total :", total)
    return total;
#Now you can call sum function
sum(10, 20);
print ("Outside the function global total :", total)