qNumericGrade=int(input("Enter your numeric grade: "))
#first if statement to check if the grade is valid
if 0 <= qNumericGrade <= 100:
    print("Your score:", qNumericGrade)
  #second if statement to check the letter grade  
    if qNumericGrade >= 90:
        lettergrade = "A"
    elif qNumericGrade >= 80:
        lettergrade = "B"
    elif qNumericGrade >= 70:
        lettergrade = "C"
    elif qNumericGrade >= 60:
        lettergrade = "D"
    else:
        lettergrade = "F"
    print("Your grade is:", lettergrade )

    if lettergrade in ["A", "B", "C"]:
        print("Excellent work congratulations on passing!")
    else:
        print("You need to improve. Keep trying!")
 #else for the first if statement qNumericGrade 
else:
    print("Invalid grade. Please enter a number between 0 and 100.")
