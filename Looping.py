#input matriks
def input_matriks(baris, kolom):
    matriks = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"Masukkan nilai [{i}][{j}]: "))
            row.append(nilai)
        matriks.append(row)
    return matriks

#tampil matriks 
def tampil(m):
    for row in m:
        for elemen in row:
            print(f"{elemen:5}", end="")
        print()

# penjumlahan & pengurangan
def tambah(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def kurang(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# perkalian
def kali(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        hasil.append(row)
    return hasil

# Menu
A = []
B = []

while True:
    print("\n=== MENU MATRIKS ===")
    print("1. Input Matriks")
    print("2. Penjumlahan")
    print("3. Pengurangan")
    print("4. Perkalian")
    print("0. Exit")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        baris = int(input("Jumlah baris: "))
        kolom = int(input("Jumlah kolom: "))

        print("\nMatriks A")
        A = input_matriks(baris, kolom)

        print("\nMatriks B")
        B = input_matriks(baris, kolom)

        print("\nMatriks A:")
        tampil(A)
        print("\nMatriks B:")
        tampil(B)

    elif pilih == "2":
        if A and B:
            print("\nHasil Penjumlahan:")
            tampil(tambah(A, B))
        else:
            print("Input matriks dulu!")

    elif pilih == "3":
        if A and B:
            print("\nHasil Pengurangan:")
            tampil(kurang(A, B))
        else:
            print("Input matriks dulu!")

    elif pilih == "4":
        if A and B:
            if len(A[0]) != len(B):
                print("Tidak bisa dikalikan! (kolom A harus = baris B)")
            else:
                print("\nHasil Perkalian:")
                tampil(kali(A, B))
        else:
            print("Input matriks dulu!")

    elif pilih == "0":
        print("Program selesai, Sampai Jumpa.")
        break

    else:
        print("Pilihan tidak valid!")