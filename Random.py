print("Random Password Generator")
#import libraries
import random
import string
#Take the input from user
length = int(input("Enter the length of Password: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
#Display
print("Your Random Password is:",password)

