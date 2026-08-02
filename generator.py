import secrets
import string
from pathlib import Path


# FILES AND SETTINGS

WORDS_FILE = Path(__file__).with_name("words.txt")

MIN_PASSWORD_LENGTH = 12
MIN_PASSPHRASE_WORDS = 4
MAX_PASSPHRASE_WORDS = 6

SEPARATORS = {
    "1": "-",
    "2": ".",
    "3": "_",
    "4": "",
}


# PASSWORD FUNCTIONS

def secure_shuffle(items):
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(items)
    return items


def generate_password(length):
    """
    Generates a password containing at least:
    - One lowercase letter
    - One uppercase letter
    - One number
    - One symbol
    """

    required_characters = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    all_characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    remaining_length = length - len(required_characters)

    additional_characters = [
        secrets.choice(all_characters)
        for _ in range(remaining_length)
    ]

    password_characters = (
        required_characters
        + additional_characters
    )

    secure_shuffle(password_characters)

    return "".join(password_characters)


# PASSPHRASE FUNCTIONS

def load_words():
    try:
        with WORDS_FILE.open("r", encoding="utf-8") as file:
            unique_words = list(
                dict.fromkeys(
                    word.strip().lower()
                    for word in file
                    if word.strip()
                )
            )

    except FileNotFoundError:
        print("\n⚠️ I could not find words.txt.")
        print("It must be in the same folder as generator.py.")
        return []

    return unique_words


def choose_separator():
    print("\nChoose a separator:")
    print("1. Hyphen       -")
    print("2. Period       .")
    print("3. Underscore   _")
    print("4. No separator")

    while True:
        choice = input("\nSelect 1, 2, 3 or 4: ").strip()

        if choice in SEPARATORS:
            return SEPARATORS[choice]

        print("⚠️ That option does not exist.")


def ask_yes_no(question):
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("⚠️ Please enter y or n.")


def generate_passphrase(
    number_of_words,
    words,
    separator,
    add_number,
    add_symbol,
):
    selected_words = secrets.SystemRandom().sample(
        words,
        number_of_words
    )

    passphrase = separator.join(selected_words)

    if add_number:
        random_number = secrets.randbelow(90) + 10
        passphrase += str(random_number)

    if add_symbol:
        random_symbol = secrets.choice(string.punctuation)
        passphrase += random_symbol

    return passphrase


# MENU FUNCTIONS

def password_menu():
    try:
        length = int(
            input(
                f"\nHow many characters do you want? "
                f"(minimum {MIN_PASSWORD_LENGTH}): "
            )
        )

    except ValueError:
        print("⚠️ Please enter a whole number.")
        return

    if length < MIN_PASSWORD_LENGTH:
        print(
            f"⚠️ Please choose at least "
            f"{MIN_PASSWORD_LENGTH} characters."
        )
        return

    password = generate_password(length)

    print("\n🔑 Your password is:")
    print(password)

    input("\nPress Enter to return to the menu...")


def passphrase_menu(words):
    try:
        amount = int(
            input(
                f"\nHow many words do you want? "
                f"({MIN_PASSPHRASE_WORDS}-"
                f"{MAX_PASSPHRASE_WORDS}): "
            )
        )

    except ValueError:
        print(
            f"⚠️ Please enter a whole number between "
            f"{MIN_PASSPHRASE_WORDS} and "
            f"{MAX_PASSPHRASE_WORDS}."
        )
        return

    if not MIN_PASSPHRASE_WORDS <= amount <= MAX_PASSPHRASE_WORDS:
        print(
            f"⚠️ Please choose between "
            f"{MIN_PASSPHRASE_WORDS} and "
            f"{MAX_PASSPHRASE_WORDS} words."
        )
        return

    if len(words) < amount:
        print(
            f"⚠️ words.txt only contains "
            f"{len(words)} unique words."
        )
        return

    separator = choose_separator()

    add_number = ask_yes_no(
        "\nWould you like to add a two-digit number?"
    )

    add_symbol = ask_yes_no(
        "Would you like to add a symbol?"
    )

    passphrase = generate_passphrase(
        amount,
        words,
        separator,
        add_number,
        add_symbol,
    )

    print("\n🔑 Your passphrase is:")
    print(passphrase)

    input("\nPress Enter to return to the menu...")


def main():
    words = load_words()

    print("🔐 RANDOM GENERATOR 3.0 🔐")

    if words:
        print(
            f"✅ {len(words):,} unique words available."
        )
    else:
        print(
            "⚠️ Passphrase generation is currently unavailable."
        )

    while True:
        print("\nWhat would you like to generate?")
        print("1. Password")
        print("2. Passphrase")
        print("3. Exit")

        option = input("\nSelect 1, 2 or 3: ").strip()

        if option == "1":
            password_menu()

        elif option == "2":
            if words:
                passphrase_menu(words)
            else:
                print(
                    "⚠️ Passphrases cannot be generated "
                    "without words.txt."
                )

        elif option == "3":
            print("\nGoodbye! 👋")
            break

        else:
            print(
                "⚠️ That option does not exist. "
                "Choose 1, 2 or 3."
            )


if __name__ == "__main__":
    main()
    