#input
nama = ["Asep", "Budi", "Cecep"]

nilai = [
    [50, 70, 40, 80],
    [78, 78, 80, 65],
    [57, 88, 67,69]
]

nim =["10121001", "10121002", "10121003"]

mk = ["MK1", "MK2", "Mk3", "MK4"]

#PROSES
#Mencari Mahasiswa terpintar
max_rata = 0
terpintar = ""

for i in range(3):
    total = 0
for j in range(4):
    total += nilai[i][j]

    rata = total / 4
    
    if rata > max_rata:
        max_rata = rata
        terpintar = nama[i]

#mencari mk dengan rata-rata terkecil
min_rata = 100
mk_kecil = ""

for j in range(4):
    total = 0
    for i in range(3):
        total += nilai[i][j]
        
    rata = total / 3
    
    if rata < min_rata:
        min_rata = rata
        mk_kecil = mk[j]

#output        
print("Mahasiswa Terpintar:", terpintar, "Nilai:", max_rata)
print("Mata Kuliah Nilai Terkecil:", mk_kecil, "Nilai:", min_rata)
