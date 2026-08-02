import secrets
import string
from pathlib import Path


# Busca words.txt en la misma carpeta donde está generator.py
WORDS_FILE = Path(__file__).with_name("words.txt")

MIN_PASSWORD_LENGTH = 12
MIN_PASSPHRASE_WORDS = 4
MAX_PASSPHRASE_WORDS = 6


def generate_password(length):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


def load_words():
    try:
        with WORDS_FILE.open("r", encoding="utf-8") as file:
            # Ignora líneas vacías y elimina duplicados.
            # "Ocean", "ocean" y "OCEAN" se consideran la misma palabra.
            unique_words = list(
                dict.fromkeys(
                    word.strip().lower()
                    for word in file
                    if word.strip()
                )
            )

    except FileNotFoundError:
        print("\n⚠️ No encontré el archivo words.txt.")
        print("Debe estar en la misma carpeta que generator.py.")
        return []

    return unique_words


def generate_passphrase(number_of_words, words):
    selected_words = secrets.SystemRandom().sample(
        words,
        number_of_words
    )

    random_number = secrets.randbelow(90) + 10

    return "-".join(selected_words) + f"-{random_number}"


print("🔐 RANDOM GENERATOR 2.0 🔐")

while True:
    print("\n¿Qué quieres generar?")
    print("1. Contraseña")
    print("2. Passphrase")
    print("3. Salir")

    option = input("\nSelecciona 1, 2 o 3: ").strip()

    if option == "1":
        try:
            length = int(
                input(
                    f"¿Cuántos caracteres quieres? "
                    f"(mínimo {MIN_PASSWORD_LENGTH}): "
                )
            )

        except ValueError:
            print("⚠️ Debes escribir un número entero.")
            continue

        if length < MIN_PASSWORD_LENGTH:
            print(
                f"⚠️ Debes escoger al menos "
                f"{MIN_PASSWORD_LENGTH} caracteres."
            )
        else:
            password = generate_password(length)

            print("\nTu contraseña es:")
            print(password)

    elif option == "2":
        try:
            amount = int(
                input(
                    f"¿Cuántas palabras quieres? "
                    f"({MIN_PASSPHRASE_WORDS}-"
                    f"{MAX_PASSPHRASE_WORDS}): "
                )
            )

        except ValueError:
            print(
                f"⚠️ Debes escribir un número entero entre "
                f"{MIN_PASSPHRASE_WORDS} y "
                f"{MAX_PASSPHRASE_WORDS}."
            )
            continue

        if not MIN_PASSPHRASE_WORDS <= amount <= MAX_PASSPHRASE_WORDS:
            print(
                f"⚠️ Debes escoger entre "
                f"{MIN_PASSPHRASE_WORDS} y "
                f"{MAX_PASSPHRASE_WORDS} palabras."
            )
            continue

        words = load_words()

        print(f"🔎 Python encontró {len(words)} palabras únicas.")

        if not words:
            print("⚠️ words.txt está vacío o Python no pudo leer sus palabras.")
            continue

        if len(words) < amount:
            print(
                f"⚠️ words.txt solo contiene "
                f"{len(words)} palabras únicas."
            )
            continue

        passphrase = generate_passphrase(amount, words)

        print("\nTu passphrase es:")
        print(passphrase)

    elif option == "3":
        print("\n¡Hasta luego! 👋")
        break

    else:
        print("⚠️ Esa opción no existe. Escoge 1, 2 o 3.")