# guess random number
import random

# define the main function
def main():
    random_guess = 1
    random_number = random.randint(1, 21)
    while random_guess != 0:
        random_guess = int(input("Guess a number between 1 and 20: "))
        if random_guess == random_number:
            print("You guessed the correct number!")
            random_guess = 0
        elif random_guess > random_number:
            print("You guessed too high!")
        elif random_guess < random_number:
            print("You guessed too low!")
        else:
            print("You guessed the wrong number!")

# call the main function
main() 
