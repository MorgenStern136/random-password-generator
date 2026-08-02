import tkinter as tk
from tkinter import messagebox, ttk

from generator import (
    MIN_PASSWORD_LENGTH,
    generate_password,
    generate_passphrase,
    load_words,
)


class GeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password & Passphrase Generator")
        self.root.geometry("680x620")
        self.root.minsize(680, 620)

        self.words = load_words()

        self.result_var = tk.StringVar()
        self.password_length_var = tk.IntVar(value=16)
        self.word_count_var = tk.IntVar(value=5)
        self.separator_var = tk.StringVar(value="-")
        self.add_number_var = tk.BooleanVar(value=True)
        self.add_symbol_var = tk.BooleanVar(value=True)
        self.status_var = tk.StringVar(value="Ready")

        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(
            self.root,
            text="🔐 Random Generator",
            font=("Arial", 22, "bold"),
        )
        title.pack(pady=(20, 5))

        subtitle = ttk.Label(
            self.root,
            text="Create secure passwords and memorable passphrases",
        )
        subtitle.pack(pady=(0, 15))

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="x", padx=30)

        password_tab = ttk.Frame(notebook, padding=20)
        passphrase_tab = ttk.Frame(notebook, padding=20)

        notebook.add(password_tab, text="Password")
        notebook.add(passphrase_tab, text="Passphrase")

        self.create_password_tab(password_tab)
        self.create_passphrase_tab(passphrase_tab)

        result_frame = ttk.LabelFrame(
            self.root,
            text="Generated result",
            padding=15,
        )
        result_frame.pack(fill="x", padx=30, pady=20)

        result_entry = tk.Entry(
            result_frame,
            textvariable=self.result_var,
            font=("Courier", 14),
            justify="center",
            state="readonly",
            background="white",
            readonlybackground="white",
            foreground="black",
            selectbackground="#3478F6",
            selectforeground="white",
            relief="solid",
            borderwidth=1,
        )
        result_entry.pack(
            fill="x",
            pady=(5, 15),
            ipady=10,
        )

        copy_button = ttk.Button(
            result_frame,
            text="Copy to clipboard",
            command=self.copy_result,
        )
        copy_button.pack()

        status_label = ttk.Label(
            self.root,
            textvariable=self.status_var,
        )
        status_label.pack(pady=(0, 10))

        word_status = ttk.Label(
            self.root,
            text=f"{len(self.words):,} unique words available",
        )
        word_status.pack()

    def create_password_tab(self, parent):
        ttk.Label(
            parent,
            text="Password length:",
        ).grid(row=0, column=0, sticky="w", padx=5, pady=10)

        length_spinbox = ttk.Spinbox(
            parent,
            from_=MIN_PASSWORD_LENGTH,
            to=128,
            textvariable=self.password_length_var,
            width=10,
        )
        length_spinbox.grid(row=0, column=1, padx=5, pady=10)

        generate_button = ttk.Button(
            parent,
            text="Generate password",
            command=self.handle_generate_password,
        )
        generate_button.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=15,
        )

    def create_passphrase_tab(self, parent):
        ttk.Label(
            parent,
            text="Number of words:",
        ).grid(row=0, column=0, sticky="w", padx=5, pady=7)

        words_spinbox = ttk.Spinbox(
            parent,
            from_=4,
            to=6,
            textvariable=self.word_count_var,
            width=10,
        )
        words_spinbox.grid(row=0, column=1, padx=5, pady=7)

        ttk.Label(
            parent,
            text="Separator:",
        ).grid(row=1, column=0, sticky="w", padx=5, pady=7)

        separator_box = ttk.Combobox(
            parent,
            textvariable=self.separator_var,
            values=("-", ".", "_", "None"),
            state="readonly",
            width=10,
        )
        separator_box.grid(row=1, column=1, padx=5, pady=7)

        number_checkbox = ttk.Checkbutton(
            parent,
            text="Add a two-digit number",
            variable=self.add_number_var,
        )
        number_checkbox.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            padx=5,
            pady=7,
        )

        symbol_checkbox = ttk.Checkbutton(
            parent,
            text="Add a symbol",
            variable=self.add_symbol_var,
        )
        symbol_checkbox.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="w",
            padx=5,
            pady=7,
        )

        generate_button = ttk.Button(
            parent,
            text="Generate passphrase",
            command=self.handle_generate_passphrase,
        )
        generate_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=15,
        )

    def handle_generate_password(self):
        try:
            length = self.password_length_var.get()
        except tk.TclError:
            messagebox.showerror(
                "Invalid length",
                "Please enter a whole number.",
            )
            return

        if length < MIN_PASSWORD_LENGTH:
            messagebox.showerror(
                "Password too short",
                f"Please choose at least {MIN_PASSWORD_LENGTH} characters.",
            )
            return

        password = generate_password(length)
        self.result_var.set(password)
        self.status_var.set("Password generated successfully")

    def handle_generate_passphrase(self):
        if not self.words:
            messagebox.showerror(
                "Words unavailable",
                "The words.txt file could not be loaded.",
            )
            return

        try:
            number_of_words = self.word_count_var.get()
        except tk.TclError:
            messagebox.showerror(
                "Invalid amount",
                "Please enter a whole number.",
            )
            return

        if not 4 <= number_of_words <= 6:
            messagebox.showerror(
                "Invalid amount",
                "Please choose between 4 and 6 words.",
            )
            return

        separator = self.separator_var.get()

        if separator == "None":
            separator = ""

        passphrase = generate_passphrase(
            number_of_words=number_of_words,
            words=self.words,
            separator=separator,
            add_number=self.add_number_var.get(),
            add_symbol=self.add_symbol_var.get(),
        )

        self.result_var.set(passphrase)
        self.status_var.set("Passphrase generated successfully")

    def copy_result(self):
        result = self.result_var.get()

        if not result:
            messagebox.showinfo(
                "Nothing to copy",
                "Generate a password or passphrase first.",
            )
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        self.root.update()

        self.status_var.set("Copied to clipboard")


def main():
    root = tk.Tk()
    GeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    