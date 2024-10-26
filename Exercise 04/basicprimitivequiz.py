#Basic primitive quiz
### Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

#Input section to answer the given question
Ans = input("What is the capital of France?")
if Ans == "Paris": #The correct or wrong answer given by the user
    print("correct answer")#If the input by the user is correct
    
#if the input by the user is wrong
else:
    print("wrong answer")
