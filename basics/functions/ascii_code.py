#The program should start by displaying the message
print ("Program Started!")

print("Please enter a standard character:")
standard_character = input() 
#print("you entered", standard_character)

if (len(standard_character) != 1):
  print("You are supposed to enter a single letter character!")
else:
  #print("correct input")
  print ("The ASCII code for", standard_character,  "is", ord(standard_character))
  cod = ord(standard_character) + 1
  print("the next character is:", chr(cod))




print("Program Ended!")