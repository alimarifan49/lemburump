import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime

def hitung_lembur():
    data = input_text.get("1.0", tk.END).strip().splitlines()
    output_text.delete("1.0", tk.END)

    total_jam = 0
    total_menit = 0

    for baris in data:
        parts = baris.split()
        if len(parts) < 5:
            continue

        try:
            tanggal_str = parts[1]
            jam_pulang_str = parts[3]
            tanggal = datetime.strptime(tanggal_str, "%Y-%m-%d")
            jam_pulang = datetime.strptime(jam_pulang_str, "%H:%M")

            hari = tanggal.weekday()  # 0=Senin ... 4=Jumat

            # Jam pulang default
            if hari == 4:  # Jumat
                jam_batas = datetime.strptime("15:00", "%H:%M")
            else:
                jam_batas = datetime.strptime("16:00", "%H:%M")

            if jam_pulang > jam_batas:
                lembur = jam_pulang - jam_batas
                jam = lembur.seconds // 3600
                menit = (lembur.seconds % 3600) // 60
                total_jam += jam
                total_menit += menit
            else:
                jam, menit = 0, 0

            hari_str = ""
            if hari == 4:  # Jumat
                hari_str = " # Jumat"

            output_text.insert(tk.END, f"{baris} {jam} jam {menit} menit{hari_str}\n")
        except Exception as e:
            output_text.insert(tk.END, f"Format error di baris: {baris}\n")

    # Konversi total menit ke jam jika lebih dari 60
    total_jam += total_menit // 60
    total_menit = total_menit % 60

    output_text.insert(tk.END, f"\nTOTAL LEMBUR = {total_jam} jam {total_menit} menit")

def show_about():
    messagebox.showinfo("About", "Develop by broAli dev\nalimarifan49@gmail.com")

# GUI setup
root = tk.Tk()
root.title("Aplikasi Hitung Jam Lembur")

# Membuat menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Menu About
menu_help = tk.Menu(menubar, tearoff=0)
menu_help.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=menu_help)

tk.Label(root, text="Paste Data Absen:").pack()

input_text = scrolledtext.ScrolledText(root, width=100, height=15)
input_text.pack()

tk.Button(root, text="Hitung Lembur", command=hitung_lembur).pack()

tk.Label(root, text="Hasil:").pack()
output_text = scrolledtext.ScrolledText(root, width=100, height=15)
output_text.pack()

root.mainloop()
