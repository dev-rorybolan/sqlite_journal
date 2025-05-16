import subprocess
import customtkinter as ctk
import bcrypt as bc

with open("password.txt", "r") as f:
    correct_password = f.read().strip().encode()

window = ctk.CTk()
window.title("Journal")
window.geometry("200x200")
window.resizable(True, True)

def main():
    if entry is not None:
        guess = entry.get().encode()
        if bc.checkpw(guess, correct_password):
            subprocess.Popen(["python3", "journal.py"])
            print("success")
            import sys
            sys.exit()
        else:

            wrong_label = ctk.CTkLabel(window, text="Wrong Password")
            wrong_label.pack()
            print("failed")

entry = ctk.CTkEntry(window)
entry.pack()
button = ctk.CTkButton(window, text="Guess", command=main)
button.pack()
window.mainloop()
