#string concat through variabe
name= "Masters "+"Dealership"
print(name)


#string concat through print statement
print("mclaren "+"P1 ")

#string concat through diff variable
a = "apollo"
b = "IE"
c = a + " " + b
print(c)

a = "mercedes"
b = "AMG"
c = "GT"
d = a+" "+b+" "+c
print(d)

#To get input from user
first_name = input ("Enter your name:")
print(first_name)

last_name = input ("Enter the last name:")
print(last_name)

ID_no = input ("Enter your BSU ID:")
print(ID_no)

Weight = int(input("Enter your weight:"))
print(Weight)

height = float(input ("Enter your height:"))
print(height)

#performing calculations
print(60+9) #for addition
print(11-9) #for subtraction
print(50*4) #for multiplication
print(69/2) #for dividing with float
print(420//2) #for dividing without float

#operator precedence BODMAS (Braket, order, division, subtraction, multiplication, addition)

print((70000*2)/4 + (50000+4000))

#to write formula in multiple line we need back slash \
result = 100000 * 40000 + 5000 * 30000 + \
                 40000 + 5000 * 30000 * 50000
print(result)

#end limiter  to remove new , by default print will switch to another statement
name = " harshin"
print (name, end =" ")
print ("First year in bathspa")

#chapter 2
#if statement
a = 1000
b = 800
if b > a:
 print("b is greater than a")
else:
 print("a is greater than b")

Salary = int (input("Enter yorur salary: "))
if Salary >= 50000:
  years_on_job = float(input("Enter the years of jobs: "))
  if years_on_job >= 2:
   print(" You are qualifed for the job ")
  else:
   print("Experience is less than 2 years")

else:
      print("You need to earn atleast 50K to qualify ")
      
#ELif
a = 600
b = 600
if b > a :
 print("b is greater than a")
elif a == b :
 print("a and b are equal")
else:
 print("a is greater than b")

#homework
score = int(input("Enter the mark: ")) 
if score >= 90:
  print("Your grade is A")
elif score >= 80:
  print("Your grade is B")
elif score >= 70:
  print("Your grade is C")
elif score >= 60:
  print("Your grade is D")
else:
  print("Your grade is F")

#Diffenrent functions have same local variables name - No syntax error 

def print_message():
  message ="hy"
  print(message)
  
def print_message_2():
  message ="hello"
  print(message)

print_message()
print_message_2()

import turtle
turtle.forward(100)
turtle.left(100)
turtle.forward(100)