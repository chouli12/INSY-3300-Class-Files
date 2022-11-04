# main function defining local variables 
def main():
    gramsFat = float(input("Please enter grams of fat =>  "))
    gramsCarbs = float(input("Please enter grams of carbs =>  "))
    cal_from_fat = gramsFat * 9
    cal_from_carbs = gramsCarbs * 4
    showCarbs(gramsFat, gramsCarbs, cal_from_fat, cal_from_carbs)

# def showCarbs | also rouding and formatting output for user..
def showCarbs(gramsFat, gramsCarbs, cal_from_fat, cal_from_carbs):
    print("Grams of fat", (f'{gramsFat:.2f}'))
    print("Fat calories", (f'{cal_from_fat:.2f}'))
    print("Grams of carbs", (f'{gramsCarbs:.2f}'))
    print("Carb calories", (f'{cal_from_carbs:.2f}'))

# calling main function
main()