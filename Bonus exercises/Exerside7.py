#Loops- Pizza Toppings : 
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 
#'quit' value. As they enter each topping, 
#Print a message saying you’ll add that topping to their pizza.

# Start a loop for pizza toppings
print("Enter the topping for the pizza. Type 'finish' to quit")

while True:
  topping = input("Enter toppings:").strip().lower()

  if topping == 'quit':
    print("Thank you for ordering! Being prepared with your topping.")
    break
  else:
      print(f"will be adding {topping} to the pizza!")
