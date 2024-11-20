## Exercise 6: Brute Force Attack - 30 Marks

#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

#Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

# Definition of correct password
perfect_password = "12345"

# Maximum number of attempts available
available_attempts = 5

# number of attempts
no_of_attempts = 0

# Use a while loop to repeatedly ask for the password until the correct one is entered or max attempts are reached
while no_of_attempts < available_attempts:
    # allowing the user to enter the password
    enter_password = input("Enter the correct password: ")

    # Check if the entered password is correct
    if enter_password == perfect_password:
        print("Access granted. Correct password entered.")
        break
    else:
        # Increment the attempt counter
        no_of_attempts += 1
        attempts_left = available_attempts - no_of_attempts
        if attempts_left > 0:
            print(f"Worong password. You have {attempts_left} attempts remaining.")
        else:
            print("Wrong password. You have reached the maximum number of attempts. Authorities have been alerted.")
            # Here you could alert the authorities if needed.
            break
