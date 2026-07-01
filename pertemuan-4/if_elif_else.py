nilai = 50 

if nilai > 85 : 
    print("Selamat kamu dapat A")
elif (nilai > 75):
    print("Selamat kamu dapat B")
else : 
    print("Selamat kamu dapat C")
    
    

number = -10 
if (number > 0) : 
    print("Positif")
elif (number < 0):
    print("Negatif")
else : 
    print("Noll")
    
""" 
- Buat program untuk menghitung konversi Suhu dari celcius ke fahrenheit, celcius ke reamur, dan celcius ke kelvin
- buat inputan suhu celciusnya menggunakan method input()
        celcius = float(input("Masukkan suhu celcius : ))
- jangan lupa konversi ke float karene input selalu bertipe string 
- print pilihan tujuan konversi, misal : 
    print("Pilih Tujuan Konversi")
    print("1: Fahrenheit")
    print("2: Reamur")
    print("3: Kelvin")
- buat inputan lagi untuk menampung pilihan dari user, mau di konversi ke apa
- buat logika pengkondisian dari user memilih konversi yang apa
- di masing masing kondisi, jika memilih 
    1. Fahrenheit, rumusnya (suhu_celcius * 9/5) + 32, lalu print "{suhu_celcius} sama dengan {suhu_fahrenheit} fahrenheit"
    2. Reamur, rumusnya suhu_celcius * 4/5, lalu print "{suhu_celcius} sama dengan {suhu_reamur} reamur"
    3. Kelvin, rumusnya suhu_celcius + 273.15, lalu print "{suhu_celcius} sama dengan {suhu_kelvin} kelvin"
- Jika pilihan tidak valid, print "Pilihan tidak valid, silahkan pilih 1, 2, atau 3"
"""
