#One of the key issue that have threatened organizations and institutions is that of name verification. 
#To solve it, people now use biometric software and machine vision enabled tools to verify identities of their employees and take attendance. 
#JT Ventures is a delivery business, with about 40 employees. 
#However, the management board would want a way to identify if a user is one of her employees. 
#Your mission, should you choose to accept it, is to write a python function program that takes a user's name and department, 
#then checks if he/she is an employee. 
#If employee exist, then welcome the employee appropriately and display the company profile 
#(jt-ventrues.csv dataset is attached) ….
#otherwise, you politely indicate that employee does not exist.
(jt-ventures.csv)

#"# importing pandas package\n",
 #   "import pandas as pd\n",
 #   " \n",
  #  "# making data frame from csv file\n",
   # "data = pd.read_csv(\"employe_records.csv\")\n",
    #"\n",
    #"# print excel\n",
    #"data"

import pandas as pd

def printinfo(jtstr):
    a = input("Enter the user's name:");
    b = input("Enter the department");
    print(a,jtstr);
    print(b,jtstr);
    return
jtstr = pd.read_csv(\"jt-ventures.csv\")\n",
#If employee exists
if

print("You are welcome to JT ventures")

#If employee dosen't exist
else
print("Unforunately the employee does not exist")
printinfo(jtstr)

