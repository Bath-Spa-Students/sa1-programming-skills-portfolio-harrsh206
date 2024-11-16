## Exercise 10: Is it even? - 35 Marks

#Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
#* The program should ask the user for a number from within the main function.
#* The entered number should be passed to a function that determines if the value is even or odd.
#* The function should return a message indicating whether the number is even or odd.
#* The message returned by the function should be printed from within the main function.

def is_it_even_or_odd(number):
    # To show if the number is even or odd
    if number % 2 == 0:
        return f"The given number {number} is even."
    else:
        return f"The given number {number} is odd."

def main():
    # Allows the user to input a number
    user_input = int(input("Please enter a number: "))
    
    # Call the function and store the result
    Answer = is_it_even_or_odd(user_input)
    
    # Prints the result
    print(Answer)

    # Ensure main runs only if the script is executed directly
if __name__ == "__main__":
    main()
