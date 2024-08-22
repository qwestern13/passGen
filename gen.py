import random
import string


def generate_password(count=5, length=12, use_digits=True, use_uppercase=True, use_lowercase=False, use_special=True):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_special:
        characters += string.punctuation
    else: 
        return characters    
    passwords = []

    for _ in range(count):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)
    
    return passwords