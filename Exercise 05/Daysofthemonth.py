## Exercise 5: Days of the Month - 30 Marks

#Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
#Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

#Define the dictionary with months and their corresponding days
months_days = {
    1:31,   #January
    2:28,   #february (will adjust for leap year)
    3:31,   #March
    4:30,   #April
    5:31,   #May
    6:30,   #June
    7:31,   #July
    8:31,   #August
    9:30,   #September
    10:31,  #October
    11:30,  #November
    12:31,  #December
}

#ask the user to input month number
month=int(input("Enter the number of the month (1-12):"))
if 1 <= month <= 12:
#Check if it's february and if the user needs leap year or not
    if month==2:
        leap=input("Checking if leap year? (yes or no):")

        if leap=='yes':
            print("This month has 29 days")
        else:
            print("This month has 28 days")
#print output of the days for the month other than fabruary
    else:
        print(f'This month has {months_days[month]} days')
else:
    print("Please enter the correct number")
