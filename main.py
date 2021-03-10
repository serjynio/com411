print ("What is your name human?")
name = input()
print ("How old are you (in years) ?")
age = int(input())
print ("How tall are you (in meters) ?")
heigh = float(input())
print ("How much do you weigh (in kilograms) ?")
weigh = float(input())
# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(f"{name} your bmi is {bmi}")