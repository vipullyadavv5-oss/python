"""Password Generator

Generate a secure random password with optional uppercase, digits, and symbols.
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """Return a generated password string."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length <= 0:
        raise ValueError("Password length must be greater than zero.")

    if not any(ch.islower() for ch in characters):
        raise ValueError("At least one lowercase character is required.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: ").strip() or "12")
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
