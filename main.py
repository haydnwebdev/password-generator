import string
import secrets
import random
import sys

length: int = 6 # minimum password length required
num_passwords: int = 6 # the number of generated passwords to output
symbols: bool = True # if password must include symbols
uppercase: bool = False # if password must include uppercase characters


def check_password_length(length: int):
    """Checks minimum length of password."""
    if length < 3:
        print("Minimum password length should be 3")
        sys.exit()


def contains_upper(password: str) -> bool:
    """Checks if password has an uppercase character within it."""
    for char in password:
        if char.isupper():
            return True

    return False


def contains_symbols(password: str) -> bool:
    """Checks if password has a symbol within it."""
    for char in password:
        if char in string.punctuation:
            return True

    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    """Checks password length, generates, and returns secure password."""
    check_password_length(length)

    # Basic combination includes lowercase and digits
    combination: str = string.ascii_lowercase + string.digits
    new_password: list = []

    # Add mandatory characters if required
    if symbols:
        combination += string.punctuation
        new_password.append(secrets.choice(string.punctuation))

    if uppercase:
        combination += string.ascii_uppercase
        new_password.append(secrets.choice(string.ascii_uppercase))

    # Ensure the length is enough to include all character types
    while len(new_password) < length:
        new_password.append(secrets.choice(combination))

    # Shuffle the password to randomize character positions
    for i in range(len(new_password)):
        j = secrets.randbelow(len(new_password))
        new_password[i], new_password[j] = new_password[j], new_password[i]

    return "".join(new_password)


if __name__ == "__main__":
    for i in range(1, num_passwords):
        new_pass: str = generate_password(length, symbols, uppercase)
        specs: str = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} -> {new_pass} ({specs})")
