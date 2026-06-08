# 1. Tipe data string
# tipe data string adalah tipe data teks/kata/karakter/kalimat
# selalu di apit oleh dua petik satu, atau dua petik dua

# contoh string diapit oleh dua petik satu ('')
print('STRING')
print('Ini adalah string yang diapit oleh petik 1')
print('Hari ini  Cerah')

# contoh string diapit oleh dua petik dua ("")
print("Ini adalah string yang diapit oleh petik 1")
print("Hari ini  Cerah")

# Jika didalam kata, mengandung karakter petik 1, untuk membuat string, harus pakai petik 2
# print('Jum'at')
print("Jum'at")

# 2.tipe data INTEGER
# Integer merupakan tipe data yang isinya angka angka numerik
# tapi dia hanya angka yang termasuk bilangan bulat
print() 
print("INTEGER")
print(500)
print(100000)
print("100000") # -> string

# 3. tipe data FLOAT
# Float ini , merupakan tipe data numerik. tapi dia bentuknya pecahan / ada koma nya
print() 
print("FLOAT")
print(50.67)
print(2.6)

# 4. Tipe data BOOLEAN (BOOL)
# Merupakan tipe data yang hanya memiliki 2 nilai (True & False)
print() 
print("BOOLEAN")
print(True) # -> Benar
print(False) # -> False


# Mengecek tipe data 
print()
print("Mengecek Tipe data")
print(type("String"))
print(type(10))
print(type(10.4))
print(type(True))