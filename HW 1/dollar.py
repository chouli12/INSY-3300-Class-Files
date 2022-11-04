# printing welcome statement
print('Welcome to The Cash Counter!!', '\n')

# promting user to enter cash value.
cash = float(input('Please Enter a Cash Value: '))
# print(cash)


# calculation for dollars
dollars = (cash * 100) // 100
print(int(dollars), "Dollars")
output1 = cash - (dollars * 1)
# print(output1)

# calculation for quaters 
quarters = (output1 % cash) // .25
print(int(quarters), "Quaters")
output2 = output1 - (quarters * .25)
# print(output2)

# calculation for dimes
dimes = (output2 % cash) // .10
# dimes = output2 / .10
print(int(dimes), "Dimes")
output3 = output2 - (dimes * .10)
# print(output3)

# calculation for nickels
nickels = round(output3 % cash, 2) // .05
# nickels = output3 / .05
print(int(nickels), "Nickels")
output4 = output3 - (nickels * .05)
# print(output4)

# calculation for pennies
pennies = round(output4, 2) / .01
# pennies = output4 / .01
print(int(pennies), "Pennies")

