import tkinter as tk
from tkinter import messagebox, ttk
import requests

def pilihan():
    usr_opt = int(opt_var.get())
    if usr_opt == 1:
        weather()
    elif usr_opt == 2:
        suhu_window()
    elif usr_opt == 3:
        segitiga()
    elif usr_opt == 4:
        shalat()
    else:
        print("Program berakhir")
        canv.destroy()

def suhu_window():
    suhu_window = tk.Toplevel(canv)
    suhu_window.title("Program Konversi Suhu")
    suhu_window.geometry("500x300")
    suhu_window.configure(bg="#E6E6FA")

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

    exit_suhu = tk.Button(suhu_window, text="Keluar", command=suhu_window.destroy, bg="#FFA07A", font=("Arial", 10))
    exit_suhu.pack(pady=5)

def weather():
    def get_weather():
        city = city_combobox.get()
        api_key = "e8991cd1702a0e52204fccb7c0db77ad" 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        return data

    def show_weather():
        weather_data = get_weather()
        
        if "message" not in weather_data:
            weather_description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            messagebox.showinfo("Cuaca", f"Cuaca di {city_combobox.get()}: {weather_description}\nSuhu: {temperature}°C")
        else:
            messagebox.showerror("Error", "Kota tidak ditemukan.")

    cuaca_window = tk.Toplevel(canv)
    cuaca_window.title("Aplikasi Cuaca")
    cuaca_window.configure(bg="#E6E6FA")
    cuaca_window.geometry("400x300")

    city_label = tk.Label(cuaca_window, text="Pilih nama kota:", bg="#E6E6FA")
    city_label.pack()

    cities = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang", "Pangkalpinang"]
    city_combobox = ttk.Combobox(cuaca_window, values=cities, state="readonly")
    city_combobox.pack()

    get_weather_button = tk.Button(cuaca_window, text="Dapatkan Cuaca", command=show_weather, bg="#ADD8E6", font=("Arial", 10))
    get_weather_button.pack(pady=10)
    
    exit_cuaca = tk.Button(cuaca_window, text="Keluar", command=cuaca_window.destroy, bg="#FFA07A", font=("Arial", 10))
    exit_cuaca.pack()

def segitiga():
    segitiga_window = tk.Toplevel(canv)
    segitiga_window.title("Program Hitung Luas Segitiga")
    segitiga_window.geometry("400x400")
    segitiga_window.configure(bg="#E6E6FA")
    
    welcome_label = tk.Label(segitiga_window, text="HITUNG LUAS SEGITIGA", font="Arial", bg="#E6E6FA")
    welcome_label.pack(pady=10)
    
    luas_label = tk.Label(segitiga_window, text="Masukan  alas segitiga: ")
    input_alas = tk.StringVar()
    input_alas_entry = tk.Entry(segitiga_window, textvariable=input_alas, font="Arial", width=10)
    luas_label.pack()
    input_alas_entry.pack()
    
    luas_label = tk.Label(segitiga_window, text="Masukan tinggi segitiga: ")
    input_tinggi = tk.StringVar()
    input_tinggi_entry = tk.Entry(segitiga_window, textvariable=input_tinggi, font="Arial", width=10)
    luas_label.pack()
    input_tinggi_entry.pack()
    
    def luas_segitiga():
        alas = float(input_alas.get())
        tinggi = float(input_tinggi.get())
        hasil = (alas * tinggi) / 2
        result_label.config(text=f"Luas segitiga adalah {hasil} ")
        
    hitung = tk.Button(segitiga_window, text="Hitung", font="Arial", command=luas_segitiga, bg="#ADD8E6")
    hitung.pack(pady=8)
    
    result_label = tk.Label(segitiga_window, text="", font=("Arial", 12), bg="#E6E6FA")
    result_label.pack(pady=10)
    
    exit_button = tk.Button(segitiga_window, text="Keluar", bg="#efefef", command=segitiga_window.destroy)
    exit_button.pack(pady=7)

def shalat():
    def dapatkan_jadwal_shalat(kota, negara):
        base_url = "http://api.aladhan.com/v1/calendarByCity"
        params = {
            "city": kota,
            "country": negara,
            "method": 2
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["data"]
        else:
            return None

    def tampilkan_jadwal_shalat():
        kota = kota_combobox.get()
        negara = "Indonesia"

        jadwal_shalat = dapatkan_jadwal_shalat(kota, negara)

        if jadwal_shalat:
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            for info_tanggal in jadwal_shalat:
                tanggal = info_tanggal["date"]["gregorian"]["date"]
                output_text.insert(tk.END, f"\nJadwal Shalat untuk {tanggal}:\n")
                for sholat, waktu in info_tanggal["timings"].items():
                    output_text.insert(tk.END, f"{sholat.capitalize()}: {waktu}\n")
            output_text.config(state=tk.DISABLED)
        else:
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Gagal mendapatkan jadwal shalat.")
            output_text.config(state=tk.DISABLED)

    root = tk.Toplevel(canv)
    root.title("Jadwal Shalat")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    kota_label = tk.Label(frame, text="Pilih Nama Kota:", bg="#E6E6FA")
    kota_label.grid(row=0, column=0, sticky="w")

    cities = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang", "Pangkalpinang"]
    kota_combobox = ttk.Combobox(frame, values=cities, state="readonly")
    kota_combobox.grid(row=0, column=1)

    get_button = tk.Button(frame, text="Dapatkan Jadwal Shalat", command=tampilkan_jadwal_shalat, bg="#ADD8E6", font=("Arial", 10))
    get_button.grid(row=1, columnspan=2, pady=6)

    output_text = tk.Text(root, height=20, width=50)
    output_text.pack(pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)
    output_text.config(state=tk.DISABLED)

    output_scrollbar = tk.Scrollbar(root, command=output_text.yview)
    output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    output_text.config(yscrollcommand=output_scrollbar.set)
    
    exit_button = tk.Button(frame, text="Keluar", command=root.destroy, bg="#FFA07A", font=("Arial", 10))
    exit_button.grid(row=2, columnspan=3, pady=6)

canv = tk.Tk()
canv.title("Program python gwehhh")
canv.geometry("300x300")
canv.configure(bg="#E6E6FA")

welcome_label = tk.Label(canv, text="Selamat datang di menu Program", bg="#E6E6FA")
welcome_label.pack(pady=10)

opt_var = tk.StringVar()
opt_var.set("1")

pilihan_opt = [
    ("Cuaca", 1),
    ("Suhu", 2),
    ("Hitung Luas Segitiga", 3),
    ("Jadwal Shalat", 4),
    ("Keluar", 5)
]

for text, value in pilihan_opt:
    tk.Radiobutton(canv, text=text, variable=opt_var, value=value, bg="#E6E6FA", font=("Arial", 10)).pack()

exec_btn = tk.Button(canv, text="Pilih", command=pilihan, bg="#ADD8E6", font=("Arial", 10))
exec_btn.pack(pady=10)

exit_btn = tk.Button(canv, text="Keluar", command=canv.destroy, bg="#FFA07A", font=("Arial", 10))
exit_btn.pack(pady=5)

canv.mainloop()
