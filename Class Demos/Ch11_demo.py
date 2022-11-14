#11-10 Inheritance
# The Automobile class holds general data
# about an automobile in inventory.

class Automobile:
    # The __init__ method accepts arguments for the
    # make, model, mileage, and price. It initializes
    # the data attributes with these values.
    
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # The following methods are mutators for the
    # class's data attributes.
    
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # The following methods are the accessors
    # for the class's data attributes.
    
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

# The Car class represents a car. It is a subclass
# of the Automobile class.

class Car(Automobile):
    # The __init__ method accepts arguments for the
    # car's make, model, mileage, price, and doors.
    
    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the __doors attribute.
        self.__doors = doors

    # The set_doors method is the mutator for the
    # __doors attribute.

    def set_doors(self, doors):
        self.__doors = doors

    # The get_doors method is the accessor for the
    # __doors attribute.

    def get_doors(self):
        return self.__doors

# The Truck class represents a pickup truck. It is a
# subclass of the Automobile class.

class Truck(Automobile):
    # The __init__ method accepts arguments for the
    # truck's make, model, mileage, price, and drive type.
    
    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the __drive_type attribute.
        self.__drive_type = drive_type

    # The set_drive_type method is the mutator for the
    # __drive_type attribute.

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # The get_drive_type method is the accessor for the
    # __drive_type attribute.

    def get_drive_type(self):
        return self.__drive_type

# The SUV class represents a sport utility vehicle. It
# is a subclass of the Automobile class.

class SUV(Automobile):
    # The __init__ method caccepts arguments for the
    # SUV's make, model, mileage, price, and passenger
    # capacity.
    
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap

    # The set_pass_cap method is the mutator for the
    # __pass_cap attribute.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # The get_pass_cap method is the accessor for the
    # __pass_cap attribute.

    def get_pass_cap(self):
        return self.__pass_cap

def main():
    # Create an object from the Car class.
    # The car is a 2007 Audi with 12,500 miles, priced
    # at $21,500.00, and has 4 doors.
    used_car = Car('Audi', 2007, 12500, 21500.00, 4)

    # Display the car's data.
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Mileage:', used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())
    print()
    
    used_car.set_price(22000.00) # new price
    print ('Updated Price:', used_car.get_price())

# Call the main function.
main()

#----------------------------------------------------------------------
#11-11, 13, 14 - Polymorphism
# The Mammal class represents a generic mammal.

class Mammal:

    # The __init__ method accepts an argument for
    # the mammal's species.
    
    def __init__(self, species):
        self.__species = species

    # The get_species method displays a message
    # indicating the mammal's species.
    
    def get_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    
    def make_sound(self):
        print('Grrrrr')

# The Dog class is a subclass of the Mammal class.

class Dog(Mammal):

    # The __init__ method calls the superclass's
    # __init__ method passing 'Dog' as the species.
    
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # The make_sound method overrides the superclass's
    # make_sound method.
    
    def make_sound(self):
        print('Woof! Woof!')
        
    def wag_tail(self):
        print('I am happy')

# The Cat class is a subclass of the Mammal class.

class Cat(Mammal):

    # The __init__ method calls the superclass's
    # __init__ method passing 'Cat' as the species.

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # The make_sound method overrides the superclass's
    # make_sound method.

    def make_sound(self):
        print('Meow')

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = Mammal('regular animal')
    dog = Dog()
    cat = Cat()

    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    # passing object as an argument 
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    
'''
    if isinstance(dog, Dog):    #slide 11-13
        dog.wag_tail()
        
    # cat.wag_tail()   #raises AttributeError
'''

# The show_mammal_info functiopn accepts an object
# as an argument, and calls its show_species
# and make_sound methods.
# slide 11-14 - passing object as an argument

def show_mammal_info(creature):
    creature.get_species()
    creature.make_sound()

# Call the main function.
main()
