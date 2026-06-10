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

nama = "zAENAL"

if nama.lower() == 'alip' : 
    print("halo alip selamat datang!")
elif nama.lower() == 'zaenal': 
    print("halo zaenal selamat datang!")
elif nama.lower() == 'erik':
    print("halo erik selamat datang!")








































