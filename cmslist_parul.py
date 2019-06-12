# PROJECT: 1, Created on- June 11,2019
# Customer Management System

#BLL
listId = []
listname = []
listaddress = []
listmob = []

def addcustomer(id, name, address, mob):
    listId.append(id)
    listname.append(name)
    listaddress.append(address)
    listmob.append(mob)

def searchCustomer(id):
    if(listId.__contains__(id)):
        ind = listId.index(id)
        print('Customer ID: ', listId[ind])
        print('Customer Name: ', listname[ind])
        print('Customer Address: ', listaddress[ind])
        print('Customer Mobile No. : ', listmob[ind])

    else:
        print('Customer not found! ')

def deleteCustomer(id):
    if(listId.__contains__(id)):
        ind = listId.index(id)
        listId.pop(ind)
        listname.pop(ind)
        listaddress.pop(ind)
        listmob.pop(ind)

    else:
        print('Customer not found! ')

def modifycust(id):
    if(listId.__contains__(id)):
        ind = listId.index(id)
        name = input("Enter Customer's new Name: ")
        address = input("Enter Customer's New Address: ")
        mob = input("Enter Customer's new number: ")
        listname.insert(ind, name)
        listaddress.insert(ind, address)
        listmob.insert(ind, mob)

    else:
        print('Customer not found!')

def showAllCustomer():
    for i in range(len(listId)):
        print('----Customer no. :', i+1, '----')
        print('Customer ID: ', listId[i])
        print('Customer Name: ', listname[i])
        print('Customer Address: ', listaddress[i])
        print('Customer Mobile no. : ', listmob[i])
1
#PL
while True:
    print("----Welcome to Customer Management System----")
    print("1. Add Customer \n 2. Search Customer \n 3. Delete \n 4. Modify \n 5. Show all the customers \n 0. Exit")
    choice = input("Enter your Choice: ")
    if(choice == '1'):
        id = (input("Enter ID"))
        name = (input("Enter Name: "))
        address = (input("Enter Address"))
        mob = (input("Enter mobile no"))
        addcustomer(id, name, address, mob) #calling
        print("Customer added successfully! ")

    elif(choice == '2'):
        id = (input("Enter Customer for Search: "))
        searchCustomer(id) #calling

    elif(choice == '3'):
        id = (input("Enter Customer ID for Deletion"))
        deleteCustomer(id)
        print("Customer deleted! ")

    elif(choice == '4'):
        id = (input("Enter Customer ID: "))
        modifycust(id)
        print("Customer modified! ")

    elif(choice == '5'):
        showAllCustomer()

    elif(choice == '6'):
        sys.exit()

    else:
        print("Invalid Choice.")