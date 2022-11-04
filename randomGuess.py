import random

#defining main function
def main():
    random_guess=1
    num=random.randint(1,21)
    while(random_guess!=0):
        random_guess = guess_answer(num)

# defining gues answer
def guess_answer(num):
    random_guess = int(input('Please enter a number between 1 and 20 or 0 to quit:  '))

    #determining if the output is high or low or same
    if random_guess > num:
        print('To high, Try again.')
    elif random_guess < num:
        print('To low, Try again.')
    elif num == random_guess:
        print("Congratulations! You guessed the right number!")
    
    #returing value to main
    return random_guess

#calling main function
main()