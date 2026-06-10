""" 
Typecasting merupakan suatu proses untuk melakukan konversi tipe data
"""

# 1. String ke int
print("Konversi String ke Integer")
""" 
Konversi dari string ke int, itu hanya bisa kalau stringnya berisi angka saja.
Jika stringnya berisi huruf, maka proses konversi akan error.
"""
number = "100"
print(f"variabel number memiliki tipe data : {type(number)} dan memiliki nilai : {number}")
# number_int = int(number)
# print(f"variabel number_int memiliki tipe data : {type(number_int)} dan memiliki nilai : {number_int}")
number = int(number)
print(f"variabel number memiliki tipe data : {type(number)} dan memiliki nilai : {number}")

# nama = "i190"
# print(f"variabel nama memiliki tipe data : {type(nama)} dan memiliki nilai : {nama}")
# nama_int = int(nama)
# print(f"variabel nama_int memiliki tipe data : {type(nama_int)} dan memiliki nilai : {nama_int}")

print()
# 2. String ke Float
print("Konversi String ke Float")
number = "19.099"
print(f"variabel number memiliki tipe data : {type(number)} dan memiliki nilai : {number}")
number_float = float(number) # 19099.0
print(f"variabel number_float memiliki tipe data : {type(number_float)} dan memiliki nilai : {number_float}")

print()
# 3. String ke Boolean
print("Konversi String ke Boolean")
nilai = "True"
print(f"variabel nilai memiliki tipe data : {type(nilai)} dan memiliki nilai : {nilai}")
nilai_bool = bool(nilai)
print(f"variabel nilai_bool memiliki tipe data : {type(nilai_bool)} dan memiliki nilai : {nilai_bool}")
nilai = ""
nilai_bool = bool(nilai)
print(f"variabel nilai_bool memiliki tipe data : {type(nilai_bool)} dan memiliki nilai : {nilai_bool}")

print()
# 4. Integer ke Float
print("Konversi Integer ke Float")
nilai = 100
print(f"variabel nilai memiliki tipe data : {type(nilai)} dan memiliki nilai : {nilai}")
nilai_float = float(nilai)
print(f"variabel nilai_float memiliki tipe data : {type(nilai_float)} dan memiliki nilai : {nilai_float}")

print()
# 5. Float ke Integer
print("Konversi Float ke Integer")
nilai = 100.78
print(f"variabel nilai memiliki tipe data : {type(nilai)} dan memiliki nilai : {nilai}")
nilai_int = int(nilai)
print(f"variabel nilai_int memiliki tipe data : {type(nilai_int)} dan memiliki nilai : {nilai_int}")