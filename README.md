# Phase 1 - Break It
"Cracking a Vigenère Cipher" - Output:
```
Ciphertext: BEFKWGKVYREQSEPKLYCMYBEFKWGKVYREQSEPKLYCMYBEFKWGKVYREQSEPKLYCMYBEFKWGK
Key(3) : KEY -> RAHASIARAHASIARAHASIARAHASIARAHASIARAHASIARAHASIARAHASIARAHASIARAHASIA
Key(7) : XRYGJZG -> ENHENHEYHTYHTYSTNSTNSENHENHEYHTYHTYSTNSTNSENHENHEYHTYHTYSTNSTNSENHENHE
Key(21) : XABGSCGRUNAMOALGHUYIU -> EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
```

"Is SHA-256 Enough to Secure Passwords?" - Output:
```
== Database ==
andi a589ffa7732ffd2f26d23953e26af5c8f6c006690b7982d5f07f671915c0b561
budi caafb8c200210ebfff71b0019004fdb01826fdd7c04b04a1fd4464c4a3868e02
citra bff5d31a5f798e5797269ea1a5923edd8cb6375ced7595ab768761eca362aebd

== Percobaan 1 ==
andi -> andi123
budi -> sayang123
citra -> bandung01

== Percobaan 2 ==
500000 hash dalam 0.3648080825805664 detik = 1370583.6681663352 hash per detik

== Percobaan 3 ==
kode7 ketemu setelah 19181014 percobaan, 49.942442655563354 detik

== Percobaan 4 ==
8 huruf kecil - 208827064576 kemungkinan -> 42.32322278827704 jam
8 huruf + angka - 2821109907456 kemungkinan -> 571.7576089378124 jam
8 karakter cetak - 6634204312890625 kemungkinan -> 1344561.863796307 jam
AES-128 (2^128) - 340282366920938463463374607431768211456 kemungkinan -> 6.896542100689128e+28 jam

== Percobaan 5 ==
Apakah tanpa salt, hash sama? True
Apakah dengan salt, hash sama? False
Hasil tebakan (walaupun ada salt): sayang123
```

This repository is the implementation of the project I shared on LinkedIn.
