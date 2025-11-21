#!/usr/bin/env python3
"""
email_validator.py

A simple script that prompts the user for an email address and checks
whether it matches basic formatting rules:
  - contains exactly one '@' character
  - has non-empty local and domain parts
  - the domain part contains at least one '.' after the '@'
"""

import re
import sys

EMAIL_REGEX = re.compile(
    r"^[^@]+@[^@]+\.[^@]+$"
)

def is_valid_email(email: str) -> bool:
    """Return True if the email matches the basic pattern."""
    return bool(EMAIL_REGEX.match(email))

def main() -> None:
    if len(sys.argv) > 1:
        email = sys.argv[1]
    else:
        email = input("Enter an email address: ").strip()

    if is_valid_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is NOT a valid email address.")

if __name__ == "__main__":
    main()
