# Def Function for finding the letter grade of score
def Grades(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else: 
        return "F"

# def function for determining the average 
def GradeAvg(score1,score2,score3, score4, score5):
    return((score1 + score2 + score3 + score4 + score5) / 5)


def main():
    #input for score 1 - score 5
    score1 = float(input("Please enter score 1 =>  "))
    score2 = float(input("Please enter score 2 =>  "))
    score3 = float(input("PLease enter score 3 =>  "))
    score4 = float(input("Please enter score 4 =>  "))
    score5 = float(input("Please enter score 5 =>  "))
    input()

    # Average grade getting sorted
    avg = GradeAvg(score1,score2,score3,score4,score5)
    
    # Formatting output for showing code
    print("Score#", "Score", "Letter Grade", sep='    ')
    print("-"*30)
    print("Score1", str(score1), Grades(score1), sep='     ')
    print("Score2", str(score2), Grades(score2), sep='     ')
    print("Score3", str(score3), Grades(score3), sep='     ')
    print("Score4", str(score4), Grades(score4), sep='     ')
    print("Score5", str(score5), Grades(score5), sep='     ')
    print("-"*30)
    print("Average", str(avg), Grades(avg), sep='    ')

main()
