import random
import string
length = int(input("Enter the length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print("Your generated password is:", password)