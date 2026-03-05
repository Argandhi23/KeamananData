# 🔐 RC4 Stream Cipher (From Scratch)

Repositori ini berisi implementasi algoritma kriptografi **RC4 (Rivest Cipher 4)** menggunakan bahasa Python murni (*from scratch*) tanpa menggunakan library kriptografi eksternal apa pun. 

Proyek ini dibuat untuk memenuhi demonstrasi tugas mata kuliah Keamanan Data / Kriptografi.

## 📝 Fitur Utama
* **100% From Scratch:** Hanya menggunakan operasi bawaan Python (List, perulangan, dan operasi bitwise XOR).
* **Visualisasi Proses:** Program tidak hanya mengenkripsi, tapi juga mencetak tahapan secara detail ke terminal, meliputi:
  * **KSA (Key-Scheduling Algorithm):** Visualisasi pengacakan *array* (S-box) 0-255 berdasarkan kunci yang diinputkan.
  * **PRGA (Pseudo-Random Generation Algorithm):** Proses pembangkitan *keystream* per byte.
  * **Operasi XOR:** Tabel visualisasi yang membandingkan Byte Input, Keystream, dan Hasil XOR secara langsung.
* **Analisis Keamanan:** Menampilkan rangkuman kelebihan dan kelemahan algoritma RC4 di akhir program.
* **Simulasi Kunci Salah:** Mendemonstrasikan bahwa dekripsi dengan kunci yang salah akan menghasilkan teks yang tetap hancur/acak.

## 🚀 Cara Menjalankan Program

Pastikan komputer Anda sudah ter-install [Python 3](https://www.python.org/downloads/).

1. *Clone* repositori ini ke komputer lokal Anda:
   ```bash
   git clone [https://github.com/Argandhi23/KeamananData.git](https://github.com/Argandhi23/KeamananData.git)
