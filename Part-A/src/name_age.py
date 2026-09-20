#!/usr/bin/env python3
"""Calculates the user's birth year based on their name and age."""

import datetime

# Get current year
current_year = datetime.datetime.now(datetime.timezone.utc).date().year


# === Main Function ===
def main() -> None:
    """Run the name-age program."""
    # Get user input
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate birth year
    birth_year = current_year - age

    # Output formatted message
    print(f"Hello {name}! You were born in {birth_year}.")


# === References ===


# === Main Guard ===
if __name__ == "__main__":
    main()
