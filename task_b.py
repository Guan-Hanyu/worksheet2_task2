try :
    grade = float(input("Please enter a number (0-100) : "))

    match grade :
        case _ if 80 <= grade <= 100:
            print("Your grade is: A ")
        case _ if 60 <= grade < 80:
            print("Your grade is: B ")
        case _ if 50 <= grade < 60:
            print("Your grade is: C ")
        case _ if 40 <= grade < 50:
            print("Your grade is: D ")
        case _ if 0 <= grade < 40:
            print("Your grade is: F ")
        case _ :
            print("Grades must be between 0 and 100.")

except :
    print("Please enter a number")
