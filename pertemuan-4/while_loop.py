number = 1

# while (kondisi):
#     ekspresi

# While akan terus berjalan selama kondisinya True / terpenuhi
# akan tetapi while akan berhenti jika kondisinya false / tidak terpenuhi
while (number < 5) : 
    print(f"Perulangan ke {number }")
    
    if number % 2 == 1 : 
        print("Bingo!")
        
    number = number + 1
    
print("Akhir dari program")

""" 
Latihan 1. 
- Buat program untuk menampilkan bilangan genap yang ada dari range 1 - 20
- print("2 adalah bilangan genap")

Latihan 2. 
- User akan menebak angka rahasia
- jumlah_tebakan = 0, angka_rahasia = 55
        tebakan_user = int(input("Masukkan tebakanmu")
- lakukan perulangan selama angka tebakan user itu tidak sama dengan angka rahasia
        while (tebakan_user != angka_rahasia)
- tebakan user menggunakan fungsi input()
        tebakan_user = int(input("Masukkan tebakanmu")        
- jika tebakan user terlalu rendah, maka print "tebakan anda terlalu rendah"
- jika tebakan user terlalu tinggi, maka print "tebakan anda terlalu tinggi"
- kita hitung juga berapa kali user telah menebak
- Kalau tebakan benar, keluar dari loop dan print 
"Selamat tebakan anda benar, angka rahasianya adalah 7 dan sudah menebak sebanyak 4 kali"


Latihan 3. 
- Buatlah program yang meminta pengguna memasukkan sebuah bilangan bulat positif N.
- Program kemudian menghitung jumlah seluruh bilangan dari 1 sampai N menggunakan while.

Contoh Output
    - Masukkan N: 5
    - Hasil penjumlahan = 15
Karena:
1 + 2 + 3 + 4 + 5 = 15


Latihan 4
- Buat program login sederhana.
- Password yang benar adalah: python123
- Pengguna diberi kesempatan maksimal 3 kali memasukkan password.

Contoh 1 (Berhasil):
    - Masukkan password: halo
    - Password salah.
    
    - Masukkan password: belajar
    - Password salah.
    
    - Masukkan password: python123
    - Login berhasil!
    
Contoh 2 (Gagal):
    - Masukkan password: abc
    - Password salah.
    
    - Masukkan password: 123
    - Password salah.
    
    - Masukkan password: qwerty
    - Password salah.

    - Akun diblokir.
"""

print()
angka = int(input("Masukkan N : "))
i = 1
hasil_akhir = 0


while (i <= angka):
    hasil_akhir = hasil_akhir + i
    # update nilai i
    i = i + 1
    
print(f"Hasil penjumlahan : {hasil_akhir}")

# misal angka = 5, i = 1, hasil akhir = 0

# Iterasi 1 : nilai i = 1, angka = 5, hasil akhir = 1, nilai i setelah update = 2
# iterasi 2 : nilai i = 2, angka = 5, hasil akhir = 3, nilai i setelah update = 3
# iterasi 3 : nilai i = 3, angka = 5, hasil akhir = 6, nilai i setelah update = 4
# iterasi 4 : nilai i = 4, angka = 5, hasil akhir = 10, nilai i setelah update = 5
# iterasi 5 : nilai i = 5, angka = 5, hasil akhir = 15, nilai i setelah update = 6


print()
password_benar = "python123"
input_user = ""
z = 0 
while (input_user != password_benar):
    input_user = input("Masukkan Password : ")
    
    z = z + 1

    if (input_user != password_benar):
        print("Password Salah")
    else :
        print("Login Berhasil!")
        
    
if (z >= 3):
    print("\nAkun diblokir")