
from datetime import datetime
import read
import bill
import write
myDictionary=read.read_txt()
currentdate=datetime.now()


def rent():
        purchased_items=[]
        want_more=True
        while want_more==True:
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N.\t\t item Name \t\t\t\t Company Name \t\t\t Price \t\t Quantity")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            file= open("products.txt","r")
            a=1
            for line in file:
                print(a,"\t\t"+line.replace(",","\t\t"))
                a=a+1
            print("------------------------------------------------------------------------------------------------------------------------------------")
            file.close()
            print("\n")
            # Valid ID 
            while True:
                try:
                    valid_id=int(input("Please Provide the ID of the item you want to rent: "))
                    if valid_id < 1 or valid_id > len(myDictionary):
                        print("Please provide a valid itemID!!!")
                    else:    
                        break
                except ValueError:
                    print("Please provide a valid itemID!!!")

            valid_id=valid_id - 1 

            #Valid Quantity
            while True:
                try:
                    user_quantity = int(input("Please Provide the number of quantity of item you want to rent: "))
                    get_quantity_of_selected_item = myDictionary[valid_id][4]
                    if user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_item):
                        print("Dear Admin, the quantity you looking for is not available in our shop.Please check the Stock")
                    else:
                        break
                except ValueError:
                    print("Enter only numbers")
       
        #update the textfile
            myDictionary[valid_id][4]= int(myDictionary[valid_id][4])-int(user_quantity)
            write.writedic(myDictionary)

        #getting user purchased items
            print(myDictionary[valid_id])
            name_of_product = myDictionary[valid_id][1]
            quantity_selected_by_user = user_quantity
            unit_price = myDictionary[valid_id][3]
            price_of_selected_item = myDictionary[valid_id][3].replace("$",'')
            total_price = int(price_of_selected_item)*int(quantity_selected_by_user)
            brand = myDictionary[valid_id][2]
            purchased_items.append([name_of_product,quantity_selected_by_user,unit_price,total_price,brand])
            user_req = input("Dear user do you want to borrow any more item? If yes press,'Y'else press 'Enter': ").upper()
            print("\n")
            if user_req=="Y":
                    print("\n")
                    want_more=True
            else:
                    total = 0
                    bill.print_bill_to_console(purchased_items)
                    want_more=False


def return_eq():
        purchased_items=[]
        want_more=True
        while want_more==True:
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N.\t\t item Name \t\t\t\t Company Name \t\t\t Price \t\t\t Quantity")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            file= open("products.txt","r")
            a=1
            for line in file:
                print(a,"\t\t"+line.replace(",","\t\t"))
                a=a+1
            print("------------------------------------------------------------------------------------------------------------------------------------")
            file.close()
            print("\n")

            # Valid ID 
            while True:
                try:
                    valid_id=int(input("Please Provide the ID of the item you want to rent: "))
                    if valid_id < 1 or valid_id > len(myDictionary):
                        print("Please provide a valid itemID!!!")
                    else:    
                        break
                except ValueError:
                    print("Please provide a valid itemID!!!")
            valid_id=valid_id - 1 

            #Valid Quantity
            while True:
                try:
                    user_quantity = int(input("Please Provide the number of quantity of item you want to rent: "))
                    get_quantity_of_selected_item = myDictionary[valid_id][4]
                    if user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_item):
                        print("Dear Admin, the quantity you looking for is not available in our shop.Please check the Stock")
                    else:
                        break
                except ValueError:
                    print("Enter only numbers")
            
        #update the textfile   
            myDictionary[valid_id][4]= int(myDictionary[valid_id][4])+int(user_quantity)
            write.writedic(myDictionary)

        #getting user purchased items
            name_of_product = myDictionary[valid_id][1]
            quantity_selected_by_user = user_quantity
            unit_price = myDictionary[valid_id][3]
            price_of_selected_item = myDictionary[valid_id][3].replace("$",'')
            total_fine=int(price_of_selected_item)*quantity_selected_by_user
            brand = myDictionary[valid_id][2]
            purchased_items.append([name_of_product,quantity_selected_by_user,unit_price,total_fine,brand])
            user_req = input("Dear user do you want to return any more item? If yes press,'Y' else press 'Enter': ").upper()
            print("\n")
            if user_req=="Y":
                    print("\n")
                    want_more=True
            else:
                    bill.print_bill_to_console_fine(purchased_items)
                    want_more=False