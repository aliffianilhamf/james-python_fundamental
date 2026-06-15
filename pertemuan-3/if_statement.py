""" 
If Statement (Pengkondisian)
Merupakan sebuah statement yang digunakan untuk mengecek suatu nilai, apakah dia True atau False. 
Jika nilai / ekspresi yang dibandingkan bernilai True, maka kode yang ada diblock if akan dieksekusi
Jika nilainya false, maka kode yang di block if akan di skip, dan kembali ke program utama

"""

usia = 17

if ( usia >= 18 ) :
    print("Dewasa")

if (usia >= 12):
    print("Remaja")

if (usia > 5):
    print("Anak - Anak")


# if (usia >= 18 ):
#     print("Dewasa") 
    
# if ((usia >= 12) and (usia < 18)):
#     print("Remaja")
    
# if ((usia > 5) and (usia < 12)):
#     print("Anak - Anak")
    
    
print("Program Selesai!")

""" 
Latihan S0al 1. 
- diketahui sebuah bilangan = 30 --> simpan ke sebuah variable
- buat program untuk mengecek 
    a. Apakah bilangan tersebut genap -> print({angka} merupakan bilangan genap)
    b. Apakah bilangan tersebut ganjil -> print({angka} merupakan bilangan ganjil)
    c. Apakah bilangan tersebut genap Positif -> print({angka} merupakan bilangan genap positif)
    d. apakah bilangan tersebut genap negatif -> print({angka} merupakan bilangan genap negatif)
    e. Apakah bilangan tersebut ganjil positif -> print({angka} merupakan bilangan ganjil positif)
    f. Apakah bilangan tersebut ganjil negatif -> print({angka} merupakan bilangan ganjil negatif)

"""

print()
# Rumus untuk mengecek apakah angka itu ganjil atau genap adalah dengan menggunakan modulo 2 
# Jika angka genap di modulo 2 akan menghasilkan 0 
# Jika angka ganjil di modulo 2 akan menghasilkan 1

# 3 % 2 = 1 --> 3 // 2 = 1 --> 2 * 1 = 2 --> 3 - 2 = 1
# 5 % 2 = 1 --> 5 // 2 = 2 --> 2 * 2 = 4 --> 5 - 4 = 1
# 10 % 2 = 0 --> 10 // 2 = 5 --> 2 * 5 = 10 --> 10 - 10 = 0 
# 13 % 2 = 1 --> 13 // 2 = 6 --> 2 * 6 = 12 --> 13 - 12 = 1
bilangan = -31

if (bilangan % 2 == 0):
    print(f"{bilangan} merupakan bilangan genap")
    
if (bilangan % 2 == 1):
    print(f"{bilangan} merupakan bilangan ganjil")
    
if ((bilangan % 2 == 0) and (bilangan > 0)):
    print(f"{bilangan} merupakan bilangan genap positif ")
    
if ((bilangan % 2 == 0) and (bilangan < 0)):
    print(f"{bilangan} merupakan bilangan genap negatif ")
    
if ((bilangan % 2 == 1) and (bilangan > 0)):
    print(f"{bilangan} merupakan bilangan ganjil positif ")
    
if ((bilangan % 2 == 1) and (bilangan < 0)):
    print(f"{bilangan} merupakan bilangan ganjil negatif ")