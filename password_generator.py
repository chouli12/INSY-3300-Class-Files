import random  

def main():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upeer_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,./<>?"
    all = lower_case + upeer_case + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    print("New Password:", ("\n\n"), password)

main()

