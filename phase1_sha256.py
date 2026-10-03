import hashlib
import os
import time

def hitung_hash(teks):
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()

users = {"andi": "andi123", "budi": "sayang123", "citra": "bandung01"}

db = {}
for user in users:
    password_asli = users[user]
    db[user] = hitung_hash(password_asli)

print("== Database ==")
for user in db:
    print(user, db[user])

#Experiment 1
wordlist = ["123456", "sayang123", "indonesia", "bandung01", "andi123", "admin", "semangat", "jakarta"]

tabel_tebakan = {}
for kata in wordlist:
    hash_kata = hitung_hash(kata)
    tabel_tebakan[hash_kata] = kata

print("\n== Percobaan 1 ==")
for user in db:
    hash_target = db[user]
    if hash_target in tabel_tebakan:
        print(user, "->", tabel_tebakan[hash_target])
    else:
        print(user, "-> tidak ditemukan")

#Experiment 2
jumlah_percobaan = 500000
mulai = time.time()
for i in range(jumlah_percobaan):
    teks = str(i)
    hashlib.sha256(teks.encode()).digest()
selesai = time.time()

waktu_total = selesai - mulai
kecepatan = jumlah_percobaan / waktu_total
print("\n== Percobaan 2 ==")
print(jumlah_percobaan, "hash dalam", waktu_total, "detik =", kecepatan, "hash per detik")

#Experiment 3
def angka_ke_teks(angka, alfabet, panjang):
    teks = ""
    basis = len(alfabet)
    for posisi in range(panjang):
        teks = alfabet[angka % basis] + teks
        angka = angka // basis
    return teks

alfabet = "abcdefghijklmnopqrstuvwxyz0123456789"
target = hitung_hash("kode7")

mulai = time.time()
ditemukan = None
percobaan = 0
for panjang in range(1, 6):
    jumlah_kombinasi = len(alfabet) ** panjang
    for angka in range(jumlah_kombinasi):
        tebakan = angka_ke_teks(angka, alfabet, panjang)
        percobaan = percobaan + 1
        if hitung_hash(tebakan) == target:
            ditemukan = tebakan
            break
    if ditemukan:
        break
selesai = time.time()

print("\n== Percobaan 3 ==")
print(ditemukan, "ketemu setelah", percobaan, "percobaan,", selesai - mulai, "detik")

#Experiment 4
print("\n== Percobaan 4 ==")
daftar_ukuran = [
    ("8 huruf kecil", 26 ** 8),
    ("8 huruf + angka", 36 ** 8),
    ("8 karakter cetak", 95 ** 8),
    ("AES-128 (2^128)", 2 ** 128),
]
for nama, ukuran in daftar_ukuran:
    jam = ukuran / kecepatan / 3600
    print(nama, "-", ukuran, "kemungkinan", "->", jam, "jam")

#Experiment 5
print("\n== Percobaan 5 ==")
password_a = "sayang123"
password_b = "sayang123"
print("Apakah tanpa salt, hash sama?", hitung_hash(password_a) == hitung_hash(password_b))

salt_a = os.urandom(16)
salt_b = os.urandom(16)
hash_a = hashlib.sha256(salt_a + password_a.encode()).hexdigest()
hash_b = hashlib.sha256(salt_b + password_b.encode()).hexdigest()
print("Apakah dengan salt, hash sama?", hash_a == hash_b)

hasil_tebak = None
for kata in wordlist:
    coba_hash = hashlib.sha256(salt_a + kata.encode()).hexdigest()
    if coba_hash == hash_a:
        hasil_tebak = kata
        break
print("Hasil tebakan (walaupun ada salt):", hasil_tebak)