#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.8\n")
#
# Question 1
# This exercise pertains to the so-called Birthday Paradox, which you can read 
# about at http://en.wikipedia.org/wiki/Birthday_paradox .
# 
# If there are 23 students in your class, what are the chances that two of you 
# have the same birthday? You can estimate this probability by generating random
# samples of 23 birthdays and checking for matches.
# 
# Hint: you can generate random birthdays with the randint function in the 
# random module.
#`

from random import randint
def birthday(student_num):
    birthdaydate = []
    for i in range(student_num):
        birthdaydate.append(randint(1, 366))
    return birthdaydate

def birthday_match(birthdaydate):
    birthdaydate.sort()
    for i in range(len(birthdaydate) - 1):
        if birthdaydate[i] == birthdaydate[i + 1]:
            return True
    return False
    
def chances(test_num, student):
    count = 0
    for i in range(test_num):
        birthdaydate = birthday(student)
        if birthday_match(birthdaydate):
            count += 1

    print('The chances that two of the class have the same birthday:',(count/test_num)*100,'%')
    


chances(65535, 23)

