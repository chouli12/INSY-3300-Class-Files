#Creating Employee class
class employee:

    # The __init__ method initializes the attributes for the Employee class
    def __init__(self, Name, ID_Number, Department, Job_Title):
        self.__Name = Name
        self.__ID_Number = ID_Number
        self.__Department = Department
        self.__Job_Title = Job_Title

    #Setters for attributes
    def set_Name(self, Name):
        self.__Name = Name

    def set_ID_Number(self, ID_Number):
        self.__ID_Number = ID_Number

    def set_Department(self, Department):
        self.__Department = Department

    def set_Job_Title(self, Job_Title):
        self.__Job_Title = Job_Title
    
    #Getters for attributes
    def get_Name(self):
        return self.__Name

    def get_ID_Number(self):
        return self.__ID_Number
    
    def get_Department(self):
        return self.__Department
    
    def get_Job_Title(self):
        return self.__Job_Title
    
def main():
    #Employee information for employee 1, 2, and 3
    Employee1 = employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    Employee2 = employee('Mark Jones', 39119, 'IT', 'Programmer')
    Employee3 = employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    #Using for loop and elif statement to print employee information
    for Employee in [Employee1, Employee2, Employee3]:
        if Employee == Employee1:
            print('Employee 1:')
        elif Employee == Employee2:
            print('Employee 2:')
        elif Employee == Employee3:
            print('Employee 3:')
        print('Name:', Employee.get_Name())
        print('ID Number:', Employee.get_ID_Number())
        print('Department:', Employee.get_Department())
        print('Title:', Employee.get_Job_Title())
        print()
main()