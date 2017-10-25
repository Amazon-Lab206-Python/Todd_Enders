import random

def scores():
    print "Scores and Grades"
    for num in range(10):
        score = random.randint(60,100)
        if score >= 60 and score < 70:
            grade = "D"
        elif score < 80:
            grade = "C"
        elif score < 90:
            grade = "B"
        else:
            grade = "A"
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

scores()