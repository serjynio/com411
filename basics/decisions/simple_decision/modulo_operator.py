# Ask user for a number 
print("Please enter a whole number.")
number = int(input()) 

# Display relevant message
if (number % 2 == 0):
    print("\nThe number {} is an even number.".format(number))
else:
    print("\nThe number {} is an odd number.".format(number))
