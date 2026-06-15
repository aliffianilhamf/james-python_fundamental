""" 
Format Specifier adalah salah satu cara untuk mengontrol output dari suatu string
tidak mengubah nilai aslinya, hanya mengatur tampilan outputnya

"""

# 1. Mengatur nilai presisi / jumlah angka di belakang koma
nilai_pi = 3.14159265 
# mengatur 3 angka dibelang koma 
print(f"Nilai PI (3 desimal) : {nilai_pi:.3f}")
print(f"Nilai PI (5 desimal) : {nilai_pi:.5f}")

# 2. memformat ribuan 
harga = 1250000 #--> Rp. 1,250,000.00
print(f"harga barang : Rp. {harga:,.2f}")

# 3. menampilan persentase 
persentase_diskon = 0.05 
print(f"Diskon : {persentase_diskon:.0%}")

# 4. mengatur perataan dan lebar kolom suatu teks 
nama = "Junaidi"
print(f"Nama siswa (rata kiri) : '{nama:<15}'")
print(f"Nama siswa (rata kanan) : '{nama:>15}'")
print(f"Nama siswa (rata tengah) : '{nama:^15}'")