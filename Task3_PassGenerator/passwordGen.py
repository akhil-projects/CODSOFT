#  Task 3 Password Generator :

import random
import string

def generate_password(length, complexity="medium"):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if complexity == "low":
        characters = lowercase + digits
    elif complexity == "medium":
        characters = lowercase + uppercase + digits
    elif complexity == "high":
        characters = lowercase + uppercase + digits + symbols
    else:
        raise ValueError(" Your Passwords Complexity must be 'low', 'medium', or 'high'")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    complexity = input("Enter complexity (low/medium/high): ").lower()

    password = generate_password(length, complexity)
    print(f"Your generated password is: {password}")