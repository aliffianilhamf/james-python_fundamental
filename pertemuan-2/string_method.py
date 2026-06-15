# Memanipulasi huruf 
teks = 'HAri iNi haTiKU seNANG'

print(f"Original    : {teks}")
print(f"Lower       : {teks.lower()}")

teks_lower = teks.lower()
print(f"Lower (variable)  : {teks_lower}")

# print(f"Original    : {teks}")
print(f"Upper       : {teks.upper()}")
print(f"Title       : {teks.title()}")
print(f"Capitalize  : {teks.capitalize()}")
print(f"Swapcase    : {teks.swapcase()}")

print()
# Pembersihan spasi 
data_kotor = "  Data ini Mengandung spasi       "
print(f"Original    : '{data_kotor}'")
print(f"Strip        : '{data_kotor.strip()}'")
print(f"Lstip       : '{data_kotor.lstrip()}'")
print(f"Rstip       : '{data_kotor.rstrip()}'")

# nama = "zAENAL"

# if nama.lower() == 'alip' : 
#     print("halo alip selamat datang!")
# elif nama.lower() == 'zaenal': 
#     print("halo zaenal selamat datang!")
# elif nama.lower() == 'erik':
#     print("halo erik selamat datang!")


print() 
judul = "Belajar Python Fundamental"
judul_split = judul.split(" ")
print(f"Original Teks : {judul}")
print(f"Setelah di split : {judul_split}")

kode_barang = "XII-ABC-778"
kode_split = kode_barang.split("-")
print(f"Original Teks : {kode_barang}")
print(f"Setelah di split : {kode_split}")

print() 
string_1 = "Python3"
# isalnum --> mengecek apakah suatu string berisi alpha numerik - campuran huruf dan angka
print(f"Apakah alnum ? : {string_1.isalnum()}")
# isalpha --> mengecek apakah suatu string berisi alpha saja - hanya huruf
print(f"Apakah is alpha ? : {string_1.isalpha()}")
# isdigit --> mengecek apakah suatu string berisi angka saja 
print(f"Apakah angka saja ? : {string_1.isdigit()}")

nama = "Heri Susanto 59"
if (nama.isalpha() == False) : 
    print("Masukkan namamu yang sebenarnya, jangan ada angkanya!")
    
print()
kode_barang = "XII-ABC-778"
kode_replace = kode_barang.replace("-","+")
print(f"Original Teks : {kode_barang}")
print(f"Setelah di replace : {kode_replace}")

nama_bersih = nama.replace(" 59", "").upper()
print(f"Original Teks : {nama}")
print(f"Setelah di replace : {nama_bersih}")

""" 
Latihan Soal 1. 
Bersihkan spasi diawal /akhir dan ubah menjadi huruf kecil semua 
- input : " JaKaRtA  "
- target : "jakarta"

Latihan Soal 2. 
Hapus "Rp" (termasuk spasi setelah Rp) dan hapus tanda titik "."
- input : "Rp 15.000.000"
- Target : "15000000"

Latihan Soal 3.
Pecah String berdasarkan karakter strip (-)
- input : "IPHONE13-RED-256GB"
- Target : ['IPHONE13', 'RED', '256GB']

Latihan Soal 4. - coba cari di google cara menggabungkan string
gabungkan list menggunakan separator tanda hubung (-)
- input : ['belajar', 'python', 'untuk', 'pemula']
- target : "belajar-python-untuk-pemula"

Latihan Soal 5. 
Pisahkan string berdasarkan |, bersihkan spasi diawal dan akhir setiap item, ubah jadi huruf kecil, ubah spase di tengah menjadi udnerscore (_), hapus tanda kurung
- input : " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
- target : ['nama_customer_', '_total_belanja_idr_', '_alamat_pengiriman']
"""

print()
soal_1 = " JaKaRtA  "
print(f"Jawaban : {soal_1.strip().lower()}")

soal_2 = "Rp 15.000.000"
print(f"Jawaban : {soal_2.replace('Rp ', '').replace('.', '')}")

soal_3 = "IPHONE13-RED-256GB"
print(f"Jawaban : {soal_3.split('-')}")

soal_4 = ['belajar', 'python', 'untuk', 'pemula']
print(f"Jawaban : {'-'.join(soal_4)}")

soal_5 =  " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
print(f"Jawaban : {soal_5.strip().lower().replace(' ', '_').replace('(', '').replace(')', '').split('|')}")







































