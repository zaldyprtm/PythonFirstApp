import tkinter as tk
from tkinter import messagebox
from tkinter import *
import requests
from tkinter import Tk, Entry, Button, StringVar
import json
import datetime
from PIL import ImageTk, Image


def pilihan():
    usr_opt = int(opt_var.get())
    if usr_opt == 1:
        weather()
    elif usr_opt == 2:
        suhu_window()
    elif usr_opt == 3:
        segitiga()
    
    else:
        print("Program berakhir")
        canv.destroy()

def suhu_window():
    # Function untuk menampilkan jendela suhu
    suhu_window = tk.Toplevel(canv)
    suhu_window.title("Program Konversi Suhu")
    suhu_window.geometry("500x300")
    suhu_window.configure(bg="#E6E6FA")  # Background color

    welcome_label = tk.Label(suhu_window, text="PROGRAM KONVERSI SUHU", font=("Arial", 16), bg="#E6E6FA")
    welcome_label.pack(pady=10)

    celcius_label = tk.Label(suhu_window, text="Masukkan suhu dalam celcius:", bg="#E6E6FA")
    celcius_label.pack()

    celcius_entry = tk.Entry(suhu_window)
    celcius_entry.pack()

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

    convert_to_reamur_button = tk.Button(suhu_window, text="Celcius ke Reamur", command=convert_to_reamur, bg="#ADD8E6", font=("Arial", 10))
    convert_to_reamur_button.pack(pady=5)

    convert_to_fahrenheit_button = tk.Button(suhu_window, text="Celcius ke Fahrenheit", command=convert_to_fahrenheit, bg="#ADD8E6", font=("Arial", 10))
    convert_to_fahrenheit_button.pack(pady=5)

    convert_to_kelvin_button = tk.Button(suhu_window, text="Celcius ke Kelvin", command=convert_to_kelvin, bg="#ADD8E6", font=("Arial", 10))
    convert_to_kelvin_button.pack(pady=5)

    result_label = tk.Label(suhu_window, text="", font=("Arial", 12), bg="#E6E6FA")
    result_label.pack(pady=10)

    # Tombol Keluar
    exit_suhu = tk.Button(suhu_window, text="Keluar", command=suhu_window.destroy, bg="#FFA07A", font=("Arial", 10))
    exit_suhu.pack(pady=5)

# cuaca
def weather():
    def get_weather(city):
        api_key = "e8991cd1702a0e52204fccb7c0db77ad"  # Ganti dengan kunci API OpenWeatherMap Anda
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        return data

    def show_weather():
        city = city_entry.get()
        weather_data = get_weather(city)
        
        if weather_data["cod"] == 200:
            weather_description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            messagebox.showinfo("Cuaca", f"Cuaca di {city}: {weather_description}\nSuhu: {temperature}°C")
        else:
            messagebox.showerror("Error", "Kota tidak ditemukan.")

    # GUI
    cuaca_window = tk.Toplevel(canv)
    cuaca_window.title("Aplikasi Cuaca")
    cuaca_window.configure(bg="#E6E6FA")  # Background color
    cuaca_window.geometry("400x300")

    city_label = tk.Label(cuaca_window, text="Masukkan nama kota:", bg="#E6E6FA")
    city_label.pack()

    city_entry = tk.Entry(cuaca_window)
    city_entry.pack()

    get_weather_button = tk.Button(cuaca_window, text="Dapatkan Cuaca", command=show_weather, bg="#ADD8E6", font=("Arial", 10))
    get_weather_button.pack(pady=10)
    
    exit_cuaca = tk.Button(cuaca_window, text="Keluar", command=cuaca_window.destroy, bg="#FFA07A", font=("Arial", 10))
    exit_cuaca.pack()

# luas segitiga
def segitiga():
    # function menampilkan window luas segitiga
    segitiga_window = tk.Toplevel(canv)
    segitiga_window.title("Program Hitung Luas Segitiga")
    segitiga_window.geometry("400x400")
    segitiga_window.configure(bg="#E6E6FA")
    
    welcome_label = tk.Label(segitiga_window, text="HITUNG LUAS SEGITIGA", font="Arial", bg="#E6E6FA")
    welcome_label.pack(pady=10)
    
    luas_label = tk.Label(segitiga_window, text="Masukan  alas segitiga: ")
    input_alas = StringVar()
    input_alas_field = Entry(segitiga_window, textvariable=input_alas, font="Arial", width=10)
    luas_label.pack()
    input_alas_field.pack()
    
    # input user
    luas_label = tk.Label(segitiga_window, text="Masukan tinggi segitiga: ")
    input_tinggi = StringVar()
    input_tinggi_field = Entry(segitiga_window, textvariable=input_tinggi, font="Arial", width=10)
    luas_label.pack()
    input_tinggi_field.pack()
    
    def luas_segitiga():
        alas = float(input_alas_field.get())
        tinggi = float(input_tinggi_field.get())
        hasil = (alas * tinggi) / 2
        result_label.config(text=f"Luas segitiga adalah {hasil} ")
        
    hitung = tk.Button(segitiga_window, text="Hitung", font="Arial", command=luas_segitiga, bg="#ADD8E6")
    hitung.pack(pady=8)
    
    result_label = tk.Label(segitiga_window, text="", font=("Arial", 12), bg="#E6E6FA")
    result_label.pack(pady=10)
    
    exit_button = tk.Button(segitiga_window, text="Keluar", bg="#efefef", command=segitiga_window.destroy)
    exit_button.pack(pady=7)


# GUI main App
canv = tk.Tk()
canv.title("Program python gwehhh")
canv.geometry("300x300")
canv.configure(bg="#E6E6FA")  # Background color

welcome_label = tk.Label(canv, text="Selamat datang di menu Program", bg="#E6E6FA")
welcome_label.pack(pady=10)

opt_var = tk.StringVar()
opt_var.set("1")

pilihan_opt = [
    ("Cuaca", 1),
    ("Suhu", 2),
    ("Hitung Luas Segitiga", 3),
    ("Keluar", 4)
]

for text, value in pilihan_opt:
    tk.Radiobutton(canv, text=text, variable=opt_var, value=value, bg="#E6E6FA", font=("Arial", 10)).pack()

exec_btn = tk.Button(canv, text="Pilih", command=pilihan, bg="#ADD8E6", font=("Arial", 10))
exec_btn.pack(pady=10)

exit_btn = tk.Button(canv, text="Keluar", command=canv.destroy, bg="#FFA07A", font=("Arial", 10))
exit_btn.pack(pady=5)

canv.mainloop()
