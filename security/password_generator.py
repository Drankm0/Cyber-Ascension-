import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("=== PASSWORD GENERATOR ===")
length = int(input("Enter password length: "))
count = int(input("How many passwords to generate: "))

print("\nYour passwords:")
for i in range(count):
    print(f"{i+1}. {generate_password(length)}") 
