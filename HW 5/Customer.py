#Creating Superclass Person
class Person:
    #Initializing attributes for Class Person
    def __init__(self, Name, Address, Telephone_Number):
        self.__Name = Name
        self.__Address = Address
        self.__Telephone_Number = Telephone_Number

    def set_Name(self, Name):
        self.__Name = Name
    
    def set_Address(self, Address):
        self.__Address = Address
    
    def set_Telphone_Number(self, Telephone_Number):
        self.__Telephone_Number = Telephone_Number

    def get_Name(self):
        return self.__Name
    
    def get_Address(self):
        return self.__Address
    
    def get_Telphone_Number(self):
        return self.__Telephone_Number

#creating subclass called customer
class Customer(Person):
    #initializing attributes from class person
    def __init__(self, Name, Address, Telephone_Number, Customer_Number, Mailing_List):
        Person.__init__(self, Name, Address, Telephone_Number)
        self.__Customer_Number = Customer_Number
        self.__Mailing_List = Mailing_List

    def set_Customer_Number(self, Customer_Number):
        self.__Customer_Number = Customer_Number

    def set_Mailing_List(self, Mailing_List):
        self.__Mailing_List = Mailing_List
    
    def get_Customer_Number(self):
        return self.__Customer_Number

    #Boolean for Mailing List
    def on_Mailing_List(self):
        if self.__Mailing_List == 'Yes':
            return True
        else:
            return False
        
def main():
    #Input Infomration for Customer
    print('Enter Customer information:')
    Name = input('Enter the Name: ')
    Address = input('Enter the Address: ')
    Telephone_Number = input('Enter the Phone Number: ')
    Customer_Number = input('Enter the Customer Number: ')
    Mailing_List = input('Does the customer want to be on the mailing list? (Yes or No): ')
    
    #passing customer information 
    customer = Customer(Name, Address, Telephone_Number, Customer_Number, Mailing_List)

    #Print customer information
    print('Customer Information')
    print('Name: ', customer.get_Name())
    print('Address: ', customer.get_Address())
    print('Phone Number: ', customer.get_Telphone_Number())
    print('Customer Number: ', customer.get_Customer_Number())
    print('Mailing List: ', customer.on_Mailing_List())
        
main()



