import customtkinter as ctk
import sqlite3
import datetime

conn = sqlite3.connect("journal.db")
cursor = conn.cursor()
dates = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

cursor.execute("""
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
""")
conn.commit()
def add_entry(title, content):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO entries (date, title, content) VALUES (?, ?, ?)",
                   (date, title, content))
    conn.commit()
    entry.configure(state=ctk.DISABLED)
    entry2.configure(state=ctk.DISABLED)
    button.configure(state=ctk.DISABLED)
    window.after(1000, lambda: entry.configure(state=ctk.NORMAL))
    window.after(1000, lambda: entry2.configure(state=ctk.NORMAL))
    window.after(1000, lambda: button.configure(state=ctk.NORMAL))


def clear_entries():
    cursor.execute("DELETE FROM entries")
    conn.commit()
    print("All journal entries cleared.")


def show_entries():
    entries = get_entries()
    top = ctk.CTkToplevel(window)
    top.title("Past Entries")
    frame = ctk.CTkScrollableFrame(top, width=900, height=600)
    frame.pack(fill="both", expand=True)

    for e in entries:
        date, title, content = e[1], e[2], e[3]
        ctk.CTkLabel(frame, text=f"{date} — {title}", font=("Arial", 16, "bold")).pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(frame, text=content, wraplength=880, font=("Arial", 14)).pack(anchor="w", padx=10, pady=(0, 10))


def get_entries():
    cursor.execute("SELECT * FROM entries ORDER BY date DESC")
    return cursor.fetchall()
window = ctk.CTk(fg_color="#2b2b2b")
window.title("Journal")
window.geometry("1000x800")
window.resizable(True, True)

label = ctk.CTkLabel(window, text="Journal\n\nPlease enter your journal entry's title:",
                     text_color="white", fg_color="#2b2b2b")
label.pack(pady=10)

entry = ctk.CTkEntry(window, fg_color="#444444", text_color="white")
entry.pack(pady=10)

label2 = ctk.CTkLabel(window, text="Journal content:", text_color="white", fg_color="#2b2b2b")
label2.pack(pady=10)

entry2 = ctk.CTkEntry(window, fg_color="#444444", text_color="white")
entry2.pack(pady=10)

button = ctk.CTkButton(window, text="Add Entry", fg_color="#555555", text_color="white", hover_color="#666666",command=lambda: add_entry(entry.get(), entry2.get()))
button.pack(pady=10)

button2 = ctk.CTkButton(window, text="Show Entries", fg_color="#555555", text_color="white", hover_color="#666666",command=show_entries)
button2.pack(pady=10)

clear_button = ctk.CTkButton(window, text="Clear All Entries", fg_color="#aa3333", text_color="white", hover_color="#cc4444",command=clear_entries)
clear_button.pack(pady=10)
window.mainloop()