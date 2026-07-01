umur = 0

if umur > 0 :
    if umur >= 18:
        print("Dewasa")
    elif umur >= 12 : 
        print("Remaja")
    else : 
        print("Anak - Anak")
else : 
    print("Umur tidak boleh negatif atau 0!")
    
    
total_beli = float(input("Masukkan Total belanja anda : "))

print(f"Total belanja : {total_beli}")
# if total_beli > 50000:
#     diskon = 20 / 100 * total_beli
#     print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
# else : 
#     if total_beli > 10000 : 
#         diskon = 10 / 100 * total_beli
#         print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
#     else : 
#         if total_beli > 5000 : 
#             diskon = 5 / 100 * total_beli
#             print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
#         else : 
#             diskon = 0
         
            
# if total_beli > 50000:
#     diskon = 20 / 100 * total_beli
#     print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
# else : 
#     if total_beli > 10000 : 
#         diskon = 10 / 100 * total_beli
#         print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
#     elif total_beli > 5000 : 
#         diskon = 5 / 100 * total_beli
#         print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
#     else : 
#         diskon = 0

if total_beli > 50000:
    diskon = 20 / 100 * total_beli
    print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
elif total_beli > 10000 : 
    diskon = 10 / 100 * total_beli
    print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
elif total_beli > 5000 : 
    diskon = 5 / 100 * total_beli
    print(f"Selamat kamu mendapat diskon sebesar : {diskon}")
else : 
    diskon = 0
        
print(f"Total yang harus di bayar adalah : {total_beli - diskon}, karena kamu mendapat diskon sebesar {diskon}")

angka_1 = float(input("Masukkan angka 1 : "))
operator = input("Masukkan operator (+, -, x, /) : ")
angka_2 = float(input("Masukkan angka 2 : "))



if operator == '+':
    print(f"Hasil dari {angka_1} + {angka_2} adalah {angka_1 + angka_2}")
elif operator == '-' : 
    print(f"Hasil dari {angka_1} - {angka_2} adalah {angka_1 - angka_2}")
elif operator == 'x' : 
    print(f"Hasil dari {angka_1} x {angka_2} adalah {angka_1 * angka_2}")
elif operator == '/' : 
    if angka_2 != 0 : 
        print(f"Hasil dari {angka_1} / {angka_2} adalah {angka_1 / angka_2}")
    else : 
        print("Angka kedua tidak boleh nol")
else : 
    print("Operator tidak valid, please masukkan (+, -, x, /)!")