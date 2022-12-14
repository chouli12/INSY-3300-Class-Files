#defining main function
def main():
    #defining local variables
    lower_case = 0
    upper_case = 0
    digit = 0
    space = 0

    #opening file for reading
    infile = open("text.txt", "r")
    #reading each line in file and counting variables
    for line in infile:
        for ch in line:
            if ch.isupper():
                upper_case += 1
            elif ch.islower():
                lower_case += 1
            elif ch.isdigit():
                digit += 1
            elif ch.isspace():
                space += 1

    #printing results
    print("Upper case letters: ", upper_case)
    print("\nLower case letters: ", lower_case)
    print("\nDigits: ", digit)
    print("\nSpaces: ", space)

main()
