#Quiz

import time

score = 0

print("Welcome to my first quiz, What is your name?")
name = input()

print("Hello " + name + ", you will be presented with 5 questions. Best of luck!")
print(" ")
print("Please enter a,b,c or d")
print(" ")
time.sleep(1)
#Question 1
print("Q1. What colour dolphin is in the Amazon river?")
print("a. Green  b. Pink  c. Turqoise  d. Maroon")
time.sleep(1)
answer = input("Please make your choice : ")
if answer == "b" :
    print("Correct!")
    score = (score +1)
elif answer == "a" :
    print("Wrong!")
elif answer == "c" :
    print("Wrong!")
elif answer == "d" :
    print("Wrong!")

time.sleep(2)
print(" ")

#Question 2
print("Q2. How many people live in the amazon rainforest?")
print("a. 30million  b. 100million  c. 450,000  d. 10,000")
time.sleep(1)
answer = input("Please make your choice : ")
if answer == "a" :
    print("Correct!")
    score = (score +1)
elif answer == "b" :
    print("Wrong!")
elif answer == "c" :
    print("Wrong!")
elif answer == "d" :
    print("Wrong!")

time.sleep(2)
print(" ")

#Question 3
print("Q3 What is the tallest building in the world?")
print("a. Goldin Finance 117  b. Shanghai Tower  c. Lotte Tower  d. Burj Khalifa")
time.sleep(1)
answer = input("Please make your choice : ")
if answer == "d" :
    print("Correct!")
    score = (score +1)
elif answer == "a" :
    print("Wrong!")
elif answer == "c" :
    print("Wrong!")
elif answer == "b" :
    print("Wrong!")

time.sleep(2)
print(" ")

#Question 4
print("Q4 What is the biggest lake in the UK?")
print("a. Lough Neagh  b. Windermere  c. Loch Lomond  d. Rutland Water")
time.sleep(1)
answer = input("Please make your choice : ")
if answer == "a" :
    print("Correct!")
    score = (score +1)
elif answer == "b" :
    print("Wrong!")
elif answer == "c" :
    print("Wrong!")
elif answer == "d" :
    print("Wrong!")

time.sleep(2)
print(" ")

#Question 5
print("Q5. What is the longest river in the world?")
print("a. Amazon  b. Congo  c. Nile  d. Irtysh")
time.sleep(1)
answer = input("Please make your choice : ")
if answer == "c" :
    print("Correct!")
    score = (score +1)
elif answer == "b" :
    print("Wrong!")
elif answer == "a" :
    print("Wrong!")
elif answer == "d" :
    print("Wrong!")
    

print(" ")
print("Thanks for playing " + name + ", you scored " + str(score) + " out of 5!")   
