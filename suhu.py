import tkinter as tk
from tkinter import messagebox

def suhu():

    def convert_to_reamur():
        celcius = float(celcius_entry.get())
        reamur = (4/5) * celcius
        result_label.config(text=f"Suhu dalam reamur adalah {reamur} Reamur")

    def convert_to_fahrenheit():
        celcius = float(celcius_entry.get())
        fahrenheit = (9/5) * celcius
        result_label.config(text=f"Suhu dalam fahrenheit adalah {fahrenheit} Fahrenheit")

    def convert_to_kelvin():
        celcius = float(celcius_entry.get())
        kelvin = celcius + 273
        result_label.config(text=f"Suhu dalam kelvin adalah {kelvin} Kelvin")

    # GUI
    root = tk.Tk()
    root.title("Program Konversi Suhu")

    welcome_label = tk.Label(root, text="PROGRAM KONVERSI SUHU", font=("Helvetica", 16))
    welcome_label.pack(pady=10)

    celcius_label = tk.Label(root, text="Masukkan suhu dalam celcius:")
    celcius_label.pack()

    celcius_entry = tk.Entry(root)
    celcius_entry.pack()

    convert_to_reamur_button = tk.Button(root, text="Celcius ke Reamur", command=convert_to_reamur)
    convert_to_reamur_button.pack(pady=5)

    convert_to_fahrenheit_button = tk.Button(root, text="Celcius ke Fahrenheit", command=convert_to_fahrenheit)
    convert_to_fahrenheit_button.pack(pady=5)

    convert_to_kelvin_button = tk.Button(root, text="Celcius ke Kelvin", command=convert_to_kelvin)
    convert_to_kelvin_button.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Helvetica", 12))
    result_label.pack(pady=10)

    root.mainloop()
