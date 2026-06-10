# Logical Operator
print("AND")
usia = 19
punya_ktp = True 
# Syarat ikut pemilu it usia > 17 DAN punya KTP
apakah_usia_mencukupi = usia > 17
apakah_punya_ktp = punya_ktp == True 

apakah_bisa_ikut_pemilu = apakah_usia_mencukupi and apakah_punya_ktp
print("Syarat ikut pemili adalah usinya lebih dari 17 dan mempunyai KTP")
print(f"saya memiliki usia {usia}, apakah usia saya mencukupi? {apakah_usia_mencukupi} dan punya ktp? {apakah_punya_ktp}, sehingga apakah saya bisa ikut pemilu ? {apakah_bisa_ikut_pemilu}")

print()
print("OR")
nilai = 90
persentase_kehadiran = 70 
# Syarat untuk lulus itu nilanya diatas 90 atau persentase kehadiran 95% 

apakah_lulus = nilai > 90 or persentase_kehadiran > 75

print(f"Saya memiliki nilai {nilai}, persentas kehadiran {persentase_kehadiran} sehingga apakah saya lulus? {apakah_lulus}")

print()
print("OR")
nilai = 90
persentase_kehadiran = 70 
# Syarat untuk lulus itu nilanya diatas 90 atau persentase kehadiran 95% 

apakah_lulus = nilai > 90 or persentase_kehadiran > 75

print(f"Saya memiliki nilai {nilai}, persentas kehadiran {persentase_kehadiran} sehingga apakah saya lulus? {not apakah_lulus}")

""" Latihan Soal 
Sebuah aplikasi hanya mengizinkan pengguna menonton kategori dewasa untuk umur = 10 dan punya akses premium 
Buatkan ekspresi logika yang menentukan apakah pengguna bisa nonton atau tidak 
"""
