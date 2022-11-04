# defining is_prime function determining if the number is prime/not prime
def is_prime(number):
    if number == 1: 
        return "Not Prime"
    for i in range(2, number):
        if number % i == 0:
            return "Not Prime"
    return "Prime"

# defining main and range of numbers 1-10 
def main():
    #defining Number of inputs
    number=10

    # Formatting the output 
    print("Number", "Is Prime", sep='   ')
    print('------------------')
    
    # Printing the output
    for i in range(1,number+1):
        print(str(i), is_prime(i), sep='        ') 

# calling main function
main()
