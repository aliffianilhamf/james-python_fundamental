# range(stop) - akan berhenti sebelum angka stopnya
for number in range(5) :
    print(f"Perulangan ke - {number}")
    
print()
# range(start, stop) - akan mulai sesuai angkanya, dan berhenti sebelum angka stopnya
for angka in range(2,7):
    print(f"Iterasi ke-{angka}")
    

print()
# range(start,stop, step) - start sesuai dengan angka start, stop sebelum angka stop, dan loncat sebanyak step
for i in range(2, 9, 2):
    print(f"Iterasi ke - {i}")
    
    
print()
# mencari angka ganjil dari 20 - 50
for angka in range(20, 51):
    if angka % 2 == 1:
        print(f"{angka} merupakan angka ganjil")

print()
for angka in range(20,1,-1):
    print(f"Hitung ke - {angka}")

print()        
# looping list
numbers = ["alex", 2, True, 4, 5] # ini adalah list

for number in numbers:
    print(f"isi dari list numbers : {number}")
    
print()
# string 
judul = "Cakrawala Bumi"
i = 1
for character in judul : 
    if character not in "aiueo":
        print
    print(f"Looping ke {i} : {character}")
    i += 1


""" 
Latihan Soal 1. 
- kalimat = "Dokumen ini berisi latihan-latihan sederhana menggunakan Python"
- print hanya huruf konsonan saja (selain aiueo) dan juga print berapa jumlah hurufnya

Latihan Soal 2. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- cari nilai maksimum dari list diatas, tanpa menggunakan fungsi max() dari python

Latihan Soal 3. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- Hitung total nilai dari yang ada di list
"""

# min_number = 1
# numbers = [30, 23, 33, 45, 54, 6, 55]

# for number in numbers:
#     if min_number == 0 : 
#         min_number = min_number + 30 
        
#     if number < min_number : 
#         min_number = number
        
        
# print(min_number)
# min_number = 9
# numbers = [30, 23, 33, 45, 54, 6, 55]
# count = 0 

# for number in numbers:
#     if count == 0 : 
#         min_number = number 
#         count += 1 
        
#     if number < min_number : 
#         min_number = number
        
        
# print(min_number)


print()
# 1
# for i in range(1, 21):
#     print(f"{i}")

# awal = 1
# akhir = 21 

# while (awal != akhir):
#     print(awal) 
#     awal += 1

# 2
# angka = int(input("Masukkan Angka N : "))

# for i in range(1, angka + 1):
#     if i % 2 == 0:
#         print(i)

# awal = 1

# while (awal != angka + 1):
#     if awal % 2 == 0:
#         print(awal)
        
#     awal = awal + 1


print()
# 3
# angka = int(input("Masukkan faktorial : "))
# result  = 1 
# count = angka

# while count > 0:
#     result = result * count
#     count = count - 1
    
# print(f"{angka} faktorial adalah = {result}")

print()
# 4 

angka = int(input("Masukkan angka : "))
total = angka 


while (angka != 0):
    angka = int(input("Masukkan angka : "))
    total += angka
    
    
print(f"Total : {total}")

