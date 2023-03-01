#CS 175L
#Brian Mohabeer
#CalculateAverage

def main():
    score1, score2, score3, score4, score5, average = calc_average()
    grade1, grade2, grade3, grade4, grade5, average_grade = determine_grade(score1, score2, score3, score4, score5, average)
    print("Score     Numeric Grade   Letter Grade")
    print("---------------------------------------------")
    print(f"score 1:     {score1:.1f}    {grade1}")
    print(f"score 2:     {score2:.1f}    {grade2}")
    print(f"score 3:     {score3:.1f}    {grade3}")
    print(f"score 4:     {score4:.1f}    {grade4}")
    print(f"score 5:     {score5:.1f}   {grade5}")
    print(f"Average score: {average}  {average_grade}")
    


def calc_average():
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))
    average = float(score1 + score2 + score3 + score4 + score5)/5
    return score1, score2, score3, score4, score5, average


def determine_grade(score1, score2, score3, score4, score5, average):
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    average_grade = 0
#Score 1
    if score1 >= 90:
        grade1 = "A"
    elif score1 >= 80:
        grade1 = "B"
    elif score1 >= 70:
        grade1 = "C"
    elif score1 >= 60:
        grade1 = "D"
    else:
        grade1 = "F"
#Score 2
    if score2 >= 90:
        grade2 = "A"
    elif score2 >= 80:
        grade2 = "B"
    elif score2 >= 70:
        grade2 = "C"
    elif score2 >= 60:
        grade2 = "D"
    else:
        grade2 = "F"
#Score 3
    if score3 >= 90:
        grade3 = "A"
    elif score3 >= 80:
        grade3 = "B"
    elif score3 >= 70:
        grade3 = "C"
    elif score3 >= 60:
        grade3 = "D"
    else:
        grade3 = "F"
#Score 4
    if score4 >= 90:
        grade4 = "A"
    elif score4 >= 80:
        grade4 = "B"
    elif score4 >= 70:
        grade4 = "C"
    elif score4 >= 60:
        grade4 = "D"
    else:
        grade4 = "F"
#Score 5
    if score5 >= 90:
        grade5 = "A"
    elif score5 >= 80:
        grade5 = "B"
    elif score5 >= 70:
        grade5 = "C"
    elif score5 >= 60:
        grade5 = "D"
    else:
        grade5 = "F"
#Average Grade
    if average >= 90:
        average_grade = "A"
    elif average >= 80:
        average_grade = "B"
    elif average >= 70:
        average_grade = "C"
    elif average >= 60:
        average_grade = "D"
    else:
        average_grade = "F"
    return grade1, grade2, grade3, grade4, grade5, average_grade
    

main()

def repeat():
    repeat = "yes"
    while repeat == "yes":
        repeat = input("Would you like to do another calculation ('yes' or 'no')?: ")
        if repeat == "yes":
            main()
            
   

repeat()






