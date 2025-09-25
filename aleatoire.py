import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    fruit = fruit_entry.get()
    animal = animal_entry.get()
    date = date_entry.get()
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Erreur", "La longueur doit être un nombre")
        return

    criteria = [x for x in [fruit, animal, date] if x]
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    base = "".join(criteria)
    remaining_length = max(0, length - len(base))
    random_part = ''.join(random.choice(characters) for _ in range(remaining_length))
    password_list = list(base + random_part)
    random.shuffle(password_list)
    password = ''.join(password_list)

    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    result_entry.config(state="readonly")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copié", "Le mot de passe a été copié dans le presse-papier")

# ---- Fenêtre principale ----
root = tk.Tk()
root.title("🔒 Générateur de Mot de Passe")
root.geometry("400x350")
root.configure(bg="#f0f4f7")  # Fond doux

title_label = tk.Label(root, text="Générateur de Mot de Passe", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#2c3e50")
title_label.pack(pady=10)

frame_inputs = tk.Frame(root, bg="#f0f4f7")
frame_inputs.pack(pady=10)

# Champs
tk.Label(frame_inputs, text="Fruit préféré :", font=("Arial", 12), bg="#f0f4f7").grid(row=0, column=0, sticky="e", padx=5, pady=5)
fruit_entry = tk.Entry(frame_inputs, font=("Arial", 12))
fruit_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Animal préféré :", font=("Arial", 12), bg="#f0f4f7").grid(row=1, column=0, sticky="e", padx=5, pady=5)
animal_entry = tk.Entry(frame_inputs, font=("Arial", 12))
animal_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Date de naissance :", font=("Arial", 12), bg="#f0f4f7").grid(row=2, column=0, sticky="e", padx=5, pady=5)
date_entry = tk.Entry(frame_inputs, font=("Arial", 12))
date_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Longueur totale :", font=("Arial", 12), bg="#f0f4f7").grid(row=3, column=0, sticky="e", padx=5, pady=5)
length_entry = tk.Entry(frame_inputs, font=("Arial", 12))
length_entry.grid(row=3, column=1, padx=5, pady=5)

# Boutons
btn_generate = tk.Button(root, text="✨ Générer le mot de passe", command=generate_password,
                         bg="#3498db", fg="white", font=("Arial", 12, "bold"), relief="raised")
btn_generate.pack(pady=10)

result_frame = tk.Frame(root, bg="#f0f4f7")
result_frame.pack(pady=5)

result_entry = tk.Entry(result_frame, font=("Arial", 14, "bold"), width=25, justify="center")
result_entry.pack(side="left", padx=5)
result_entry.config(state="readonly")

btn_copy = tk.Button(result_frame, text="📋 Copier", command=copy_password,
                     bg="#2ecc71", fg="white", font=("Arial", 12, "bold"))
btn_copy.pack(side="left", padx=5)

root.mainloop()

