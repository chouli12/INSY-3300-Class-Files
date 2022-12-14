# #define main function
def main():
    #promt users to enter first middle and last
    first = input("Enter your first name: ")
    middle = input("Enter your middle name: ")
    last = input("Enter your last name: ")
    
    #split the first name and print the first letter
    first_name = first.split()
    print(first_name[0][0], end=".")

    #split the middle name and print the first letter
    middle_name = middle.split()
    print(middle_name[0][0], end=".")

    #split the last name and print the first letter
    last_name = last.split()
    print(last_name[0][0])

main()


