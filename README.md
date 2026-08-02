# 🔐 Random Password & Passphrase Generator

My first Python project: a terminal-based generator that creates secure random passwords and memorable passphrases.

## Features

- Generates passwords using letters, numbers, and symbols
- Generates passphrases containing 4 to 6 random words
- Uses Python's `secrets` module for secure random selection
- Loads words from an external `words.txt` file
- Ignores blank lines and duplicate words
- Prevents repeated words within the same passphrase
- Validates incorrect user input
- Works from an interactive terminal menu

## Project structure

```text
random-generator/
├── generator.py
├── words.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3
- No external packages required

## How to run it

Open a terminal in the project folder and run:

```bash
python3 generator.py
```

Then select:

```text
1. Password
2. Passphrase
3. Exit
```

## Security note

This project uses Python's `secrets` module instead of `random`, making the selections more suitable for generating passwords and passphrases.

Never share a real password or passphrase after generating it.

## Future improvements

- Custom separators
- Optional numbers and symbols
- Password-strength information
- Copy-to-clipboard button
- Graphical user interface
- Automated tests

## Author

RZ
