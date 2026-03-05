"""
================================================================
  RC4 (Rivest Cipher 4) - Implementasi dari Scratch
  Algoritma Stream Cipher
================================================================
  Dibuat untuk tugas mata kuliah Kriptografi
  
  RC4 ditemukan oleh Ron Rivest (RSA Security) tahun 1987.
  Digunakan di: SSL, WEP WiFi, Microsoft Office encryption.
  
  Cara kerja:
    1. KSA  - Key Scheduling Algorithm  → mengacak array S
    2. PRGA - Pseudo-Random Generation  → menghasilkan keystream
    3. XOR  - enkripsi / dekripsi
================================================================
"""


# ============================================================
# TAHAP 1: KSA (Key Scheduling Algorithm)
# Tujuan: Mengacak array S[0..255] berdasarkan kunci
# ============================================================
def ksa(key: str) -> list:
    """
    Key Scheduling Algorithm.
    
    Input : key (string, contoh: "secretkey")
    Output: S[] - array 256 elemen yang sudah diacak
    """
    key_bytes = [ord(c) for c in key]  # Ubah key ke list angka ASCII
    key_len   = len(key_bytes)

    # Langkah 1: Inisialisasi S = [0, 1, 2, ..., 255]
    S = list(range(256))

    print("=" * 60)
    print("TAHAP 1 — KSA (Key Scheduling Algorithm)")
    print("=" * 60)
    print(f"  Kunci         : '{key}'")
    print(f"  Kunci (ASCII) : {key_bytes}")
    print(f"  S awal (5 pertama): {S[:5]} ... {S[-3:]}")

    # Langkah 2: Acak S menggunakan kunci
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % key_len]) % 256
        S[i], S[j] = S[j], S[i]   # Tukar S[i] dan S[j]

    print(f"  S akhir (5 pertama): {S[:5]} ... {S[-3:]}")
    print("  → S berhasil diacak!\n")
    return S


# ============================================================
# TAHAP 2 & 3: PRGA + XOR (Enkripsi / Dekripsi)
# Tujuan: Hasilkan keystream lalu XOR dengan teks
# ============================================================
def prga_xor(S: list, data: bytes, mode: str = "enkripsi") -> bytes:
    """
    Pseudo-Random Generation Algorithm + XOR.
    
    Input : S[]   - array hasil KSA
            data  - bytes yang akan diproses
            mode  - "enkripsi" atau "dekripsi"
    Output: hasil bytes setelah di-XOR dengan keystream
    """
    S = S[:]   # Salin S agar tidak mengubah array asli
    i, j = 0, 0
    result = []

    print("=" * 60)
    print(f"TAHAP 2 & 3 — PRGA + XOR ({mode.upper()})")
    print("=" * 60)
    print(f"  {'Byte Input':>12} | {'Keystream':>10} | {'XOR Hasil':>10} | {'Karakter'}")
    print(f"  {'-'*12}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")

    for byte in data:
        # PRGA: generate 1 byte keystream
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]        # Tukar
        t = (S[i] + S[j]) % 256
        keystream_byte = S[t]           # 1 byte keystream

        # XOR: enkripsi atau dekripsi (rumus SAMA!)
        xor_result = byte ^ keystream_byte
        result.append(xor_result)

        # Tampilkan proses per byte
        char_out = chr(xor_result) if 32 <= xor_result <= 126 else '?'
        print(f"  {byte:>12} | {keystream_byte:>10} | {xor_result:>10} | {char_out}")

    print()
    return bytes(result)


# ============================================================
# FUNGSI UTAMA: rc4_encrypt & rc4_decrypt
# ============================================================
def rc4_encrypt(plaintext: str, key: str) -> bytes:
    """Enkripsi plaintext dengan RC4."""
    print("\n" + "█" * 60)
    print("  PROSES ENKRIPSI RC4")
    print("█" * 60)
    print(f"  Plaintext  : '{plaintext}'")
    print(f"  Kunci      : '{key}'\n")

    S          = ksa(key)
    data_bytes = plaintext.encode('utf-8')
    ciphertext = prga_xor(S, data_bytes, mode="enkripsi")

    print(f"  Ciphertext (hex) : {ciphertext.hex().upper()}")
    print(f"  Ciphertext (dec) : {list(ciphertext)}\n")
    return ciphertext


def rc4_decrypt(ciphertext: bytes, key: str) -> str:
    """
    Dekripsi ciphertext dengan RC4.
    Prosesnya IDENTIK dengan enkripsi karena sifat XOR!
    """
    print("\n" + "█" * 60)
    print("  PROSES DEKRIPSI RC4")
    print("█" * 60)
    print(f"  Ciphertext (hex) : {ciphertext.hex().upper()}")
    print(f"  Kunci            : '{key}'\n")

    S          = ksa(key)
    plaintext  = prga_xor(S, ciphertext, mode="dekripsi")
    hasil      = plaintext.decode('utf-8')

    print(f"  Plaintext hasil  : '{hasil}'\n")
    return hasil


# ============================================================
# PENJELASAN XOR (Visualisasi)
# ============================================================
def jelaskan_xor():
    print("=" * 60)
    print("KONSEP DASAR: Operasi XOR")
    print("=" * 60)
    print("  XOR truth table:")
    print("    0 XOR 0 = 0")
    print("    0 XOR 1 = 1")
    print("    1 XOR 0 = 1")
    print("    1 XOR 1 = 0  ← Inilah kunci keajaiban RC4!")
    print()
    print("  Contoh dengan huruf 'H' (ASCII 72):")
    print("    Plaintext  byte: 72   = 01001000")
    print("    Keystream  byte: 200  = 11001000")
    print("    XOR hasil       : 128  = 10000000  → Ciphertext")
    print()
    print("  Dekripsi (XOR lagi dengan keystream yang SAMA):")
    print("    Ciphertext byte: 128  = 10000000")
    print("    Keystream  byte: 200  = 11001000")
    print("    XOR hasil       :  72  = 01001000  → 'H' kembali! ✓")
    print()


# ============================================================
# ANALISIS KEAMANAN
# ============================================================
def analisis_keamanan():
    print("=" * 60)
    print("ANALISIS: Kelebihan & Kelemahan RC4")
    print("=" * 60)
    kelebihan = [
        "Sangat cepat dan ringan (cocok untuk perangkat lama)",
        "Implementasi sangat sederhana",
        "Kunci bisa sampai 2048 bit",
    ]
    kelemahan = [
        "Byte pertama keystream dapat diprediksi (lemah!)",
        "Rentan terhadap serangan Fluhrer-Mantin-Shamir (FMS)",
        "Sudah DILARANG di TLS 1.3 dan WPA3 sejak 2015",
        "Tidak aman jika kunci yang sama digunakan 2x",
    ]
    print("  ✅ KELEBIHAN:")
    for k in kelebihan:
        print(f"     • {k}")
    print()
    print("  ❌ KELEMAHAN:")
    for k in kelemahan:
        print(f"     • {k}")
    print()
    print("  📌 Kesimpulan: RC4 sudah TIDAK DIREKOMENDASIKAN")
    print("     untuk sistem modern. Gunakan AES-GCM atau ChaCha20.")
    print()


# ============================================================
# DEMO UTAMA
# ============================================================
if __name__ == "__main__":
    print("\n" + "▓" * 60)
    print("  RC4 STREAM CIPHER — Demo Implementasi dari Scratch")
    print("▓" * 60 + "\n")

    # --- Penjelasan XOR ---
    jelaskan_xor()

    # --- Input ---
    plaintext = "Hello, RC4!"
    key       = "SecretKey"

    # --- Enkripsi ---
    ciphertext = rc4_encrypt(plaintext, key)

    # --- Dekripsi ---
    hasil_dekripsi = rc4_decrypt(ciphertext, key)

    # --- Verifikasi ---
    print("=" * 60)
    print("VERIFIKASI HASIL")
    print("=" * 60)
    print(f"  Plaintext  awal   : '{plaintext}'")
    print(f"  Kunci             : '{key}'")
    print(f"  Ciphertext (hex)  : {ciphertext.hex().upper()}")
    print(f"  Hasil dekripsi    : '{hasil_dekripsi}'")
    sukses = "✅ BERHASIL" if plaintext == hasil_dekripsi else "❌ GAGAL"
    print(f"  Status            : {sukses}")
    print()

    # --- Analisis Keamanan ---
    analisis_keamanan()

    # --- Demo: kunci salah tidak bisa dekripsi ---
    print("=" * 60)
    print("DEMO TAMBAHAN: Kunci Salah → Dekripsi Gagal")
    print("=" * 60)
    kunci_salah  = "WrongKey!"
    S_salah      = ksa(kunci_salah)
    gagal_bytes  = prga_xor(S_salah, ciphertext, mode="dekripsi")
    try:
        gagal_str = gagal_bytes.decode('utf-8', errors='replace')
    except Exception:
        gagal_str = str(gagal_bytes)
    print(f"  Dengan kunci '{kunci_salah}': '{gagal_str}'")
    print("  → Hasil tidak terbaca = kriptografi bekerja! ✓\n")