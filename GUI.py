import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        total_nilai = 0
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
            total_nilai += nilai

        # Menghitung rata-rata nilai
        rata_rata = total_nilai / len(entries)
        
        # Menentukan prodi berdasarkan rata-rata nilai
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Pendidikan Bahasa"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#e8f0fe")

# Judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#e8f0fe")
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#e8f0fe")
frame_input.pack(pady=10)

# Input nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#e8f0fe")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
prediksi_button.pack(pady=30)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("nunito", 14, "italic"), fg="skyblue", bg="#e8f0fe")
hasil_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
