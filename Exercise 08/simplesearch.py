## Exercise 8: Simple Search - 30 Marks

#Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
#1. Allow the user to input the search term instead of using a predefined value.
#2. Implement the search functionality based on user input.

# The list of names
list_of_name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Allow the user to enter a name to search for
search_name = input("Please enter the name you're looking for: ")

# Searching for the name in the list
if search_name in list_of_name:
    print(f"{search_name} available in the list.")
else:
    print(f"{search_name} not available in the list.")
    
