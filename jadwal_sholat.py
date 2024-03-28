import requests
import tkinter as tk

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

def tampilkan_jadwal_shalat(kota_entry, negara_entry, output_text, output_scrollbar):
    kota = kota_entry.get()
    negara = negara_entry.get()

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

def main():
    root = tk.Tk()
    root.title("Jadwal Shalat")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    kota_label = tk.Label(frame, text="Masukkan Nama Kota:")
    kota_label.grid(row=0, column=0, sticky="w")

    kota_entry = tk.Entry(frame)
    kota_entry.grid(row=0, column=1)

    negara_label = tk.Label(frame, text="Masukkan Nama Negara:")
    negara_label.grid(row=1, column=0, sticky="w")

    negara_entry = tk.Entry(frame)
    negara_entry.grid(row=1, column=1)

    get_button = tk.Button(frame, text="Dapatkan Jadwal Shalat", command=lambda: tampilkan_jadwal_shalat(kota_entry, negara_entry, output_text, output_scrollbar))
    get_button.grid(row=2, columnspan=2)

    output_text = tk.Text(root, height=20, width=50)
    output_text.pack(pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)
    output_text.config(state=tk.DISABLED)

    output_scrollbar = tk.Scrollbar(root, command=output_text.yview)
    output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    output_text.config(yscrollcommand=output_scrollbar.set)

    root.mainloop()

if __name__ == "__main__":
    main()
