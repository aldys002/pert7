import tkinter as tk
from tkinter import ttk

# Fungsi untuk menampilkan hasil prediksi
def show_prediction():
    result_label.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x550")  # Atur ukuran jendela

# Label judul
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18), pady=10)
title_label.pack()

# Frame untuk input nilai mata pelajaran
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

# Membuat input nilai mata pelajaran
entries = []
for i in range(1, 11):
    # Label untuk setiap mata pelajaran
    label = tk.Label(input_frame, text=f"Mata Pelajaran {i}:", font=("Arial", 11), anchor="w")
    label.grid(row=i-1, column=0, padx=10, pady=5, sticky="w")
    
    # Entry untuk input nilai
    entry = ttk.Entry(input_frame, width=25)
    entry.grid(row=i-1, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk hasil prediksi
predict_button = ttk.Button(root, text="Hasil Prediksi", command=show_prediction)
predict_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()