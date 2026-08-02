# 🔐 Random Password & Passphrase Generator

My first Python project: a secure generator for creating random passwords and memorable passphrases through either a graphical interface or an interactive terminal menu.

## Features

- Generates passwords using lowercase and uppercase letters, numbers, and symbols
- Generates passphrases containing 4 to 6 random words
- Allows custom passphrase separators
- Can add an optional two-digit number and symbol to passphrases
- Uses Python's `secrets` module for secure random selection
- Loads words from an external `words.txt` file
- Ignores blank lines and duplicate words
- Prevents repeated words within the same passphrase
- Validates incorrect user input
- Includes a graphical user interface
- Includes a copy-to-clipboard button
- Can also be used through an interactive terminal menu
- Includes automated tests with GitHub Actions

## Project structure

```text
random-password-generator/
├── .github/
│   └── workflows/
│       └── main.yml
├── .gitignore
├── generator.py
├── gui.py
├── README.md
├── test_generator.py
└── words.txt
```

## Requirements

- Python 3
- Tkinter for the graphical interface
- No external Python packages required

> On some macOS installations, the system version of Python may include an outdated version of Tk. A current Python installer from [python.org](https://www.python.org/downloads/) is recommended.

## How to run it

First, download or clone the repository and open a terminal in the project folder.

### Graphical interface

Run:

```bash
python3 gui.py
```

The graphical interface lets you:

- Choose between passwords and passphrases
- Select the password length
- Select the number of words
- Choose a separator
- Add an optional number or symbol
- Generate a result
- Copy the result to the clipboard

### Terminal interface

Run:

```bash
python3 generator.py
```

Then select an option from the interactive menu:

```text
1. Password
2. Passphrase
3. Exit
```

## Running the tests

Run the automated tests with:

```bash
python3 -m unittest test_generator.py -v
```

The tests verify password length and character requirements, passphrase word counts, unique word selection, separators, and optional numbers and symbols.

GitHub Actions also runs the test suite automatically after every push or pull request.

## Security note

This project uses Python's `secrets` module instead of `random`, making its selections more suitable for generating passwords and passphrases.

Never share a password or passphrase you intend to use. Any generated result shared in screenshots, messages, documentation, or testing should be considered exposed and discarded.

The copy-to-clipboard feature temporarily places the generated result on the system clipboard. Clipboard contents may be accessible to other applications.

## Future improvements

- Password-strength information
- Option to exclude ambiguous characters
- Clear-result button
- Keyboard shortcuts
- Additional graphical-interface tests
- Improved visual design
- Packaged desktop application

## Author

MS