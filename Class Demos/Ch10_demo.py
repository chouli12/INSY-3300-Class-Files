#10.12 - Coin class example
import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    
    # The __init__ method initializes the
    # sideup data attribute with 'Heads'.
    
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
    
    def get_sideup(self):
        return self.sideup

#-----------------------------------------------------------
#10-15 Creating an instance of Coin class
    
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin...')
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    
# Call the main function.
main()

#-----------------------------------------------------------
#10-16 Public versus Private attributes
    
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin...')
    my_coin.toss()

    # But now I'm going to cheat! I'm going to
    # directly change the value of the object's
    # sideup attribute to 'Heads'.
    my_coin.sideup = 'Heads'

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    
# Call the main function.
main()

#------------------------------------------------------------
#10-16 use of private attributes with __
import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:

    # private attribute with __ prefix
    def __init__(self):
        self.__sideup = 'Heads'     

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

# The main function.
def main():
    my_coin = Coin()

    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call the main function.
main()

#-----------------------------------------------------------
#10-17 passing multiple parameters
import random

class Coin:
    
    # passing a paramter to init method
    def __init__(self, side):
        self.__sideup = side
  
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            
    # a new method for multiple tosses
    def multi_toss(self, times):
        for count in range(times):
            self.toss()
 
    def get_sideup(self):
        return self.__sideup

# The main function.
def main():
    # Create an object from the Coin class with Tails up.
    my_coin = Coin('Tails')

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin multiple times
    print('I am going to toss the coin five times:')
    my_coin.multi_toss(5)
    
    print('This side is up:', my_coin.get_sideup())
    
# Call the main function.
main()
#-----------------------------------------------------------
#10-18 __str__ method   for printing the object
import random

class Coin:
    
    def __init__(self, side):
        self.__sideup = side
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def multi_toss(self, times):
        for count in range(times):
            self.toss()
    
    def get_sideup(self):
        return self.__sideup

    # the str method to print the object status
    def __str__(self):
        return f'The coin has it {self.__sideup} up'

# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin('Tails')

    # Display the status of coin.
    print(my_coin)
    
# Call the main function.
main()
#-----------------------------------------------------
#10-19 & 22 multiple instances of the same class
# creates three instances of the Coin class.
# get and set methods
import random

class Coin:
    
    def __init__(self, side):
        self.__sideup = side
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def multi_toss(self, times):
        for count in range(times):
            self.toss()

    #getter method - Accessor
    def get_sideup(self):
        return self.__sideup

    #setter method - Mutator
    def set_sideup(self, side):
        self.__sideup = side

    # the str method to print the object status
    def __str__(self):
        return f'The coin has it {self.__sideup} up'
    
def main():
    # Create three objects from the Coin class.
    coin1 = Coin('Heads')
    coin2 = Coin('Tails')
    coin3 = Coin('Heads')

    #decided the change the sideup for coin3
    coin3.set_sideup('Tails')

    # Display the side of each coin that is facing up.
    print('I have three coins with these sides up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    
    # Toss the coin.
    print('I am tossing all three coins...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Display the side of each coin that is facing up.
    print('Now here are the sides that are up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

# Call the main function.
main()
#----------------------------------------------------------------
