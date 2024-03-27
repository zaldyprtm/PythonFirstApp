# Program cuaca dengan api OpenWheater 
import tkinter as tk
from tkinter import messagebox
import requests
import main

def get_weather(city):
    api_key = "e8991cd1702a0e52204fccb7c0db77ad"  # Ganti dengan kunci API OpenWeatherMap Anda
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def cuaca():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data["cod"] == 200:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        messagebox.showinfo("Cuaca", f"Cuaca di {city}: {weather_description}\nSuhu: {temperature}°C")
    else:
        messagebox.showerror("Error", "Kota tidak ditemukan.")

# GUI
root = tk.Tk()
root.title("Aplikasi Cuaca")

city_label = tk.Label(root, text="Masukkan nama kota:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Dapatkan Cuaca", command=show_weather)
get_weather_button.pack(pady=10)

root.mainloop()

if __name__ == '__main__':
    run()