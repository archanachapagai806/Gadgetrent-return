# \t= one tab
# \n= new line
from datetime import datetime
import read
import operation

print("\n")
print("\t \t \t \tArchana Rental")  # \t is used to give tab space
print("\n")
print("\t \t \t Kathmandu ")
print("\n")  # \n new line

print("\t \t \t \t Wel-Come to the Archana Rental!")
print("\n")


myDictionary = read.read_txt()
# print(read.read_txt())
currentdate = datetime.now()
print(currentdate)

loop = True  # initializing loop
while loop == True:
    print("Given are the options")
    print("Press 1 to rent an items")
    print("Press 2 to return items")
    print("Press 3 to Exit")
    print("\n")
    try:
        userInput = int(input("Enter the option you want to continue: "))
        if userInput == 1:
            operation.rent()
        elif userInput == 2:
            operation.return_eq()
        elif userInput == 3:
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("\t \t \t Thank You!! Visit Again!")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            break
        else:
            print("Enter the correct option")
    except ValueError:
        print("Enter the correct option")
