# Read in user data 
print("What is your name?")
name = input() 

print("What is your age?")
age = int(input())

print("What is your weight?") 
weight = float(input()) 

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print (f"{name} , your are {age} years old and your bmi is {bmi} ")

