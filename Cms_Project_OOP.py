#Creating a Customer Management System using the concept of Object Oriented Programming

#----BUSINESS LOGIC LAYER
class Customer:
    list1 = []
    def __init__(self):
        self.id = 0
        self.name = None
        self.add = None
        self.mob = None

    def addCustomer(self):
        Customer.list1.append(self)

    def search(self, id):   #id is provided in the argument so that we may get to know that on the basis of id we have to search the customer
        for e in Customer.list1:
            if e.id == id:
                self.id = e.id
                self.name = e.name
                self.add = e.add
                self.mob = e.mob
            else:
                print("Invalid ID")

    def delete(self, id):
        for e in Customer.list1:
            if e.id == id:
                i = Customer.list1.index(e)
                Customer.list1.pop(i)

    def modify(self, id):
        for e in Customer.list1:
            if e.id == id:
                self.name = input("Enter new name of the Customer: ")
                self.add = input("Enter new Address: ")
                self.mob = input("Enter new Number: ")
                e.id = self.id
                e.name = self.name
                e.add = self.add
                e.mob = self.mob

    def show(self):
        for e in Customer.list1:
            print("###########")
            print("Customer Id: ", e.id)
            print("Customer Name: ", e.name)
            print("Customer Address: ", e.add)
            print("Customer Mobile no: ", e.mob)

#----PRESENTATION LAYER----
cus = Customer()
while True:
    print("1. Add Customer \n 2. Search Customer \n 3. Delete the Customer \n 4. Modify the Customer \n 5. Show all customers \n 6. Exit")
    ch = input("Enter your Choice: ")

    if (ch == '1'):

        cus.id = int(input("Enter id: "))
        cus.name = input("Enter Name of the Customer: ")
        cus.address = input("Enter Address: ")
        cus.mob = input("Enter Mobile no.: ")
        cus.addCustomer()   #calling of functions
        print("Customer added successfully! ")

    elif (ch == '2'):

        id = int(input("Enter your id: "))
        cus.search(id)
        print("Id = ", cus.id)
        print("Name = ", cus.name)
        print("Address = ", cus.address)
        print("Mobile no = ", cus.mob)
        print("Search Successful!")

    elif (ch == '3'):

        id = int(input("Enter id for deletion: "))
        cus.delete(id)
        print("Deletion Successful!")

    elif (ch == '4'):

        id = int(input("Enter id to modify: "))
        cus.modify(id)
        print("**Modification successful**")

    elif (ch == '5'):
        cus.show()

    else:
        exit()