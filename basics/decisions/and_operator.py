# Ask user for what they saw and heard
print("What did I hear?")
hear = input() 

print("What did I see?")
see = input()

# Determine what message to display
if ( (hear == "grr") and (see == "two red eyes") ):
    print("\nThere is a scary creature. I should get out of here!")
else:
    print("\nI am a little scared but I will continue.")
