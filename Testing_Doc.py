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