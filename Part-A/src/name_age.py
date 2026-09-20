"""Calculate approximate birth year based on user input of name and age.

Input:
    - name: str, user's name from standard input.
    - age: int, user's age from standard input.

Process:
    - Retrieve current year using the datetime module.
    - Subtract user's age from the current year to estimate birth year.

Output:
    - str, personalized greeting and estimated birth year printed to standard output.

Typical usage example:
    Enter your name: Alice
    Enter your age: 33
    Hello Alice! You were born in approximately 1993.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer

# === Main Function ===
def main() -> None:
    """Run the name-age program."""
    # Get user input.
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in approximately {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()

# === References ===
# Python Software Foundation. (n.d.). Built-in Functions - input(). Python Documentation. Retrieved from https://docs.python.org/3/library/functions.html#input
# Python Software Foundation. (n.d.). datetime — Basic date and time types. Python Documentation. Retrieved from https://docs.python.org/3/library/datetime.html
