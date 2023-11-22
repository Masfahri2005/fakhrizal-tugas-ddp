# soal nomor 1
def profil(nama,alamat,gender,umur,hobby):
    print("nama saya adalah",nama)
    print("alamat saya,alamat")
    print(gender)
    print("umur saya",umur)
    print("hobby saya adalah",hobby)
profil("fakhrizal","bojonggede","laki-laki","19","hiking")

# soal nomor 2
def tentukan_nilai_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

# cetak nilai kelulusan
nilai = 70
print(tentukan_nilai_kelulusan(nilai))

#soal nomor 3
def cetak_bilangan_ganjil(batas):
    for nilai in range(1, batas + 1, 2):
     print(nilai)

# Cetak batas tertinggi
batas_tertinggi = 10
cetak_bilangan_ganjil(batas_tertinggi)

