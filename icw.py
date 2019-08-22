# #problem 1
import random
# numGen= random.randint(1,100)
# print(numGen)

#Problem 2
# userInput=input("Enter a word: ")
# while(userInput!="q"):
#     userInput=input("Enter a word: ")
#
#
# #problem 4
numRand=random.randint(1,10)
user_guess=-2

while user_guess!=numRand:
    user_guess=int(input("Enter your guess: "))
    if user_guess!=numRand:
          print("Incorrect")
    else:
        print("Correct")

