## Exercise 7: Some Counting - 20 Marks

#Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
#in each case.
#* Write a loop that counts up from 0 to 50 in increments of 1.
#* Write a loop that counts down from 50 to 0 in decrements of 1.
#* Write a loop that counts up from 30 to 50 in increments of 1.
#* Write a loop that counts down from 50 to 10 in decrements of 2.
#* Write a loop that counts up from 100 to 200 in increments of 5.
#*You may include all loops in a single project*

# 1. Loop that counts up from 0 to 50 in the increments of 1
print("Counting starts from 0 to 50:")
for Jumbo in range(0, 51, 1):
    print(Jumbo)

# 2. Loop that counts down from 50 to 0 in the decrements of 1
print("\nCounting starts from 50 to 0:")
for Jumbo in range(50, -1, -1):
    print(Jumbo)

# 3. Loop that counts up from 30 to 50 in the increments of 1
print("\nCounting starts from 30 to 50:")
for Jumbo in range(30, 51, 1):
    print(Jumbo)

# 4. Loop that counts down from 50 to 10 in the decrements of 2
print("\nCounting down from 50 to 10, decreasing by 2 each time:")
for Jumbo in range(50, 9, -2):
    print(Jumbo)

# 5. Loop that counts up from 100 to 200 in the increments of 5
print("\nCounting starts from 100 to 200 in increments of 5 each time:")
for Jumbo in range(100, 201, 5):
    print(Jumbo)