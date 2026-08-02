import string
import unittest

from generator import (
    generate_password,
    generate_passphrase,
)


class TestPasswordGenerator(unittest.TestCase):

    def test_password_has_requested_length(self):
        password = generate_password(16)

        self.assertEqual(len(password), 16)

    def test_password_contains_lowercase_letter(self):
        password = generate_password(20)

        self.assertTrue(
            any(character.islower() for character in password)
        )

    def test_password_contains_uppercase_letter(self):
        password = generate_password(20)

        self.assertTrue(
            any(character.isupper() for character in password)
        )

    def test_password_contains_number(self):
        password = generate_password(20)

        self.assertTrue(
            any(character.isdigit() for character in password)
        )

    def test_password_contains_symbol(self):
        password = generate_password(20)

        self.assertTrue(
            any(
                character in string.punctuation
                for character in password
            )
        )


class TestPassphraseGenerator(unittest.TestCase):

    def setUp(self):
        self.words = [
            "velvet",
            "ocean",
            "crimson",
            "sparrow",
            "forest",
            "silver",
            "lunar",
            "maple",
        ]

    def test_passphrase_contains_requested_words(self):
        passphrase = generate_passphrase(
            number_of_words=5,
            words=self.words,
            separator="-",
            add_number=False,
            add_symbol=False,
        )

        selected_words = passphrase.split("-")

        self.assertEqual(len(selected_words), 5)

    def test_passphrase_does_not_repeat_words(self):
        passphrase = generate_passphrase(
            number_of_words=6,
            words=self.words,
            separator="-",
            add_number=False,
            add_symbol=False,
        )

        selected_words = passphrase.split("-")

        self.assertEqual(
            len(selected_words),
            len(set(selected_words)),
        )

    def test_passphrase_uses_selected_separator(self):
        passphrase = generate_passphrase(
            number_of_words=4,
            words=self.words,
            separator="_",
            add_number=False,
            add_symbol=False,
        )

        self.assertEqual(passphrase.count("_"), 3)

    def test_passphrase_can_add_number(self):
        passphrase = generate_passphrase(
            number_of_words=4,
            words=self.words,
            separator="-",
            add_number=True,
            add_symbol=False,
        )

        self.assertTrue(passphrase[-2:].isdigit())

    def test_passphrase_can_add_symbol(self):
        passphrase = generate_passphrase(
            number_of_words=4,
            words=self.words,
            separator="-",
            add_number=False,
            add_symbol=True,
        )

        self.assertIn(passphrase[-1], string.punctuation)


if __name__ == "__main__":
    unittest.main()
    