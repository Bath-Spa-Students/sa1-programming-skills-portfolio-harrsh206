## Exercise 3: Biography - 25 Marks

#In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single `print()` statement.
#3. Use variables with appropriate data types for each piece of information.



### Advanced Requirements:
#Have the user input their name, hometown, and age instead of hardcoding the values.
#Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
#Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?

name=input("please enter your name:") #To enter the users name 
hometown=input("please enter your hometown:") #To enter the users hometown
age=input("please enter your age:") #To eneter users age
Data ={"name": name,"hometown":hometown,"age": age} #The data that will output as the display
print(Data["name"]) #To Display the name
print(Data["hometown"]) #To display the hometown
print(Data["age"]) #To display the age
