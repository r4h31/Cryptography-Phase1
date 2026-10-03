from math import gcd

CIPHERTEXT = "BEFKWGKVYREQSEPKLYCMYBEFKWGKVYREQSEPKLYCMYBEFKWGKVYREQSEPKLYCMYBEFKWGK"

ENGLISH_FREQ = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
    'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
    'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074}

INDO_FREQ = {
    'A': 14.6, 'B': 2.4, 'C': 1.6, 'D': 3.9, 'E': 9.3, 'F': 0.3,
    'G': 3.5, 'H': 3.0, 'I': 7.9, 'J': 0.2, 'K': 4.8, 'L': 4.0,
    'M': 3.3, 'N': 7.7, 'O': 2.0, 'P': 3.0, 'Q': 0.0, 'R': 4.9,
    'S': 6.0, 'T': 4.4, 'U': 3.3, 'V': 0.2, 'W': 1.3, 'X': 0.0,
    'Y': 1.6, 'Z': 0.0}

def bersihkan(teks):
    teks = teks.upper()
    hasil = ""
    for c in teks:
        if c.isalpha():
            hasil += c
    return hasil

def vigenere_decrypt(ciphertext, key):
    result = ""
    key_index = 0
    for ch in ciphertext:
        shift = ord(key[key_index % len(key)]) - ord('A')
        result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        key_index += 1
    return result

def cari_repetisi(teks, panjang=3):
    posisi = {}
    for i in range(len(teks) - panjang + 1):
        pola = teks[i:i + panjang]
        if pola not in posisi:
            posisi[pola] = []
        posisi[pola].append(i)

    hasil = {}
    for pola in posisi:
        if len(posisi[pola]) > 1:
            hasil[pola] = posisi[pola]
    return hasil

def hitung_jarak(repetisi):
    jarak = {}
    for pola in repetisi:
        posisi = repetisi[pola]
        gap = []
        for j in range(1, len(posisi)):
            gap.append(posisi[j] - posisi[j - 1])
        jarak[pola] = gap
    return jarak

def faktor(n):
    hasil = []
    for f in range(2, n + 1):
        if n % f == 0:
            hasil.append(f)
    return hasil

def kandidat_panjang_kunci(teks):
    jarak = hitung_jarak(cari_repetisi(teks))

    semua_jarak = []
    for pola in jarak:
        for g in jarak[pola]:
            semua_jarak.append(g)

    if len(semua_jarak) == 0:
        return []

    fpb = semua_jarak[0]
    for g in semua_jarak[1:]:
        fpb = gcd(fpb, g)

    return faktor(fpb)

FREKUENSI = ENGLISH_FREQ   #dapat diganti ke ENGLISH_FREQ kalau ciphertext-nya bahasa Inggris

def shift_terbaik(kolom):
    skor = {}
    for s in range(26):
        total = 0
        for c in kolom:
            huruf = chr((ord(c) - 65 - s) % 26 + 65)
            total += FREKUENSI[huruf]
        skor[s] = total
    shift_pilihan = 0
    skor_tertinggi = -1
    for s in skor:
        if skor[s] > skor_tertinggi:
            skor_tertinggi = skor[s]
            shift_pilihan = s
    return chr(shift_pilihan + 65)

def cari_kunci(teks, panjang):
    kunci = ""
    for i in range(panjang):
        kolom = ""
        for j in range(i, len(teks), panjang):
            kolom += teks[j]
        kunci += shift_terbaik(kolom)
    return kunci

teks = bersihkan(CIPHERTEXT)
print("Ciphertext:", teks)

for L in kandidat_panjang_kunci(teks):
    kunci = cari_kunci(teks, L)
    hasil = vigenere_decrypt(teks, kunci)
    print(f"Key({L}) :", kunci, "->", hasil)