# RC4 (Rivest Cipher 4) — Implementasi dari Scratch

> Tugas Mata Kuliah Kriptografi  
> Implementasi algoritma **RC4 Stream Cipher** menggunakan Python 3 tanpa library enkripsi eksternal.

---

## 📋 Deskripsi

Repository ini berisi implementasi lengkap algoritma **RC4 (Rivest Cipher 4)** dari scratch sebagai bagian dari tugas mata kuliah Kriptografi. Program mendemonstrasikan seluruh tahapan RC4 secara step-by-step:

1. **KSA** (Key Scheduling Algorithm) — pengacakan array state berdasarkan kunci
2. **PRGA** (Pseudo-Random Generation Algorithm) — pembangkitan keystream
3. **Enkripsi** — XOR plaintext dengan keystream
4. **Dekripsi** — XOR ciphertext dengan keystream yang sama

---

## 📁 Struktur Repository

```
rc4-kriptografi/
├── rc4_implementation.py   # Implementasi utama RC4 dari scratch
├── README.md               # Dokumentasi ini
└── laporan/
    └── TugasKripto_[Nama]_[NIM]_RC4.pdf   # Laporan tertulis (PDF)
```

---

## ⚙️ Cara Menjalankan

### Prasyarat
- Python 3.x (tidak membutuhkan library tambahan)

### Langkah-langkah

**1. Clone repository ini:**
```bash
git clone [URL_REPOSITORY_KAMU]
cd rc4-kriptografi
```

**2. Jalankan program:**
```bash
python3 rc4_implementation.py
```

**3. Output yang akan muncul:**
```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  RC4 STREAM CIPHER — Demo Implementasi dari Scratch
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

[TAHAP 1 - KSA]  → Array S diacak berdasarkan kunci
[TAHAP 2 - PRGA] → Keystream dihasilkan per byte
[TAHAP 3 - XOR]  → Enkripsi & Dekripsi

Plaintext  : 'Hello, RC4!'
Ciphertext : 5C DD 50 2B B0 5E 3E F0 A7 27 1C
Dekripsi   : 'Hello, RC4!'
Status     : ✅ BERHASIL
```

---

## 🔑 Cara Kerja RC4

```
KUNCI  ──►  KSA  ──►  S[] teracak
                           │
                           ▼
PLAINTEXT ──►  PRGA + XOR  ──►  CIPHERTEXT

CIPHERTEXT ──►  PRGA + XOR  ──►  PLAINTEXT
                 (proses identik)
```

### Tahap 1: KSA (Key Scheduling Algorithm)
```python
# Inisialisasi
S = list(range(256))
K = [ord(c) for c in key] * (256 // len(key) + 1)

# Pengacakan
j = 0
for i in range(256):
    j = (j + S[i] + K[i]) % 256
    S[i], S[j] = S[j], S[i]  # swap
```

### Tahap 2 & 3: PRGA + XOR
```python
i, j = 0, 0
for byte in data:
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    keystream_byte = S[(S[i] + S[j]) % 256]
    result = byte ^ keystream_byte  # XOR
```

---

## ✅ Kelebihan RC4

| Aspek | Keterangan |
|-------|-----------|
| Kecepatan | Sangat cepat, cocok perangkat terbatas |
| Implementasi | Sederhana dan ringkas |
| Fleksibilitas kunci | 40 bit hingga 2048 bit |

## ❌ Kelemahan RC4

| Kelemahan | Keterangan |
|-----------|-----------|
| Bias keystream | Byte pertama dapat diprediksi |
| Serangan FMS | Rentan Fluhrer-Mantin-Shamir Attack (2001) |
| Reuse kunci | Tidak boleh pakai kunci sama dua kali |
| Status | Dilarang di TLS 1.3 dan WPA3 sejak 2015 |

---

## 🎥 Demo Video

> Link video demo / screen record program berjalan:  
> **[URL_VIDEO_DEMO_KAMU]**

---

## 📄 Laporan

> Link laporan PDF:  
> **[URL_LAPORAN_PDF_KAMU]**

---

## 📚 Referensi

- Rivest, R. L. (1992). *The RC4 Encryption Algorithm*. RSA Data Security, Inc.
- Fluhrer, S., Mantin, I., & Shamir, A. (2001). *Weaknesses in the Key Scheduling Algorithm of RC4*. SAC 2001.
- RFC 7465 — Prohibiting RC4 Cipher Suites. IETF, 2015.
- Stallings, W. (2017). *Cryptography and Network Security* (7th ed.). Pearson.

---

## 👤 Identitas

| | |
|--|--|
| **Nama** | Faqih Rafasha Arganddhi |
| **NIM** | 25051204263 |
| **Mata Kuliah** | Keamanan Data dan Informasi |
| **Algoritma** | RC4 — Stream Cipher Simetris |
